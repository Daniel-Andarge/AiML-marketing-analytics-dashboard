import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Initialize an empty list to store the data
data = []

# Define the range of post numbers to loop through
start_post = 70000
end_post = 87823

# Define the keywords to check for
keywords = ['#BOA', '#WegagenBank', '#CBE', '#AwashBank', '#Hibretbank', '#GlobalBankEthiopia']

# Helper function to convert views to numbers
def convert_views(views_str):
    views_str = views_str.replace(',', '')  # Remove commas if present
    if 'K' in views_str:
        views = float(views_str.replace('K', '')) * 1000
    elif 'M' in views_str:
        views = float(views_str.replace('M', '')) * 1000000
    elif 'B' in views_str:
        views = float(views_str.replace('B', '')) * 1000000000
    else:
        views = float(views_str)
    return int(views)

for post_num in range(start_post, end_post + 1):
    try:
        # Construct the URL for each post
        channel_url = f'https://t.me/tikvahethiopia/{post_num}?embed=1&mode=tme'
        
        # Send a request to the Telegram channel's web page
        response = requests.get(channel_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract messages
        messages = soup.find_all('div', class_='tgme_widget_message')
        
        for message in messages:
            try:
                # Check if any of the keywords are in the message
                for keyword in keywords:
                    if keyword in message.get_text():
                        try:
                            post_link = message.find('a', class_='tgme_widget_message_date')['href']
                        except Exception:
                            post_link = None
                        
                        try:
                            date = message.find('time')['datetime']
                        except Exception:
                            date = None
                        
                        try:
                            views_str = message.find('span', class_='tgme_widget_message_views').text if message.find('span', class_='tgme_widget_message_views') else '0'
                            views = convert_views(views_str)
                        except Exception:
                            views = None
                        
                        try:
                            post_time = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').time().strftime('%H:%M:%S')
                        except Exception:
                            post_time = None
                        
                        try:
                            bank = keyword  # Use the keyword as the bank name
                        except Exception:
                            bank = None
                        
                        try:
                            hour = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').hour
                            if hour < 12:
                                time_of_day = 'morning'
                            elif hour < 18:
                                time_of_day = 'afternoon'
                            else:
                                time_of_day = 'evening'
                        except Exception:
                            time_of_day = None

                        data.append([post_link, date, views, post_time, bank, time_of_day])
            except Exception as e:
                print(f"Error processing message {post_num}: {e}")
    except Exception as e:
        print(f"Error fetching post {post_num}: {e}")

# Create a DataFrame
df = pd.DataFrame(data, columns=['post_link', 'date', 'views', 'post_time', 'bank', 'time_of_day'])

# Specify the folder path to save the CSV file
folder_path = os.path.join(os.getcwd(), '..', 'data')  # Go one level up from the current directory to 'data' folder
csv_path = os.path.join(folder_path, 'banks_telegram_posts_data.csv')

# Check if the folder exists, if not create it
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Save to CSV
df.to_csv(csv_path, index=False) 