import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


data = []

max_posts = 100

keyword = '#BankofAbyssinia'

def convert_views(views_str):
    views_str = views_str.replace(',', '')  
    if 'K' in views_str:
        views = float(views_str.replace('K', '')) * 1000
    elif 'M' in views_str:
        views = float(views_str.replace('M', '')) * 1000000
    elif 'B' in views_str:
        views = float(views_str.replace('B', '')) * 1000000000
    else:
        views = float(views_str)
    return int(views)


posts_processed = 0


post_num = 1
while posts_processed < max_posts:
    try:
        # Construct the URL for the latest post
        channel_url = f'https://t.me/tikvahethiopia/{post_num}?embed=1&mode=tme'
        
        # Send a request to the Telegram channel's web page
        response = requests.get(channel_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract messages
        messages = soup.find_all('div', class_='tgme_widget_message')
        
        for message in messages:
            try:

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
                        keyword_found = keyword
                    except Exception:
                        keyword_found = None
                    
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

                    data.append([post_link, date, views, post_time, keyword_found, time_of_day])
                    posts_processed += 1
                    if posts_processed >= max_posts:
                        break
            except Exception as e:
                print(f"Error processing message {post_num}: {e}")
    except Exception as e:
        print(f"Error fetching post {post_num}: {e}")
    
    post_num += 1

df = pd.DataFrame(data, columns=['post_link', 'date', 'views', 'post_time', 'ad_type', 'time_of_day'])

folder_path = os.path.join(os.getcwd(), '..', 'data') 
csv_path = os.path.join(folder_path, 'telegram_ads_data.csv')

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

df.to_csv(csv_path, index=False)