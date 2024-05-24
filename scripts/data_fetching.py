from google_play_scraper import Sort, reviews_all
import pandas as pd

import os
import sys
def fetch_app_reviews(app_id):
    """
    Fetches app reviews from  Google Play store.

    Args:
        app_id (str): The app ID for which to fetch reviews.

    Returns:
        pandas.DataFrame: A DataFrame containing the app reviews.

    Raises:
        Exception: If an error occurs while fetching the app reviews.
    """
    try:
      
        result = reviews_all(
            app_id,
            sleep_milliseconds=0,
             lang='en',
            country='us',
            sort=Sort.NEWEST,
            filter_score_with=None 
        )
        # Convert to Pandas DataFrame
        df = pd.DataFrame(result)

       
        return df

    except Exception as e:
        print(f"Error occurred while fetching app reviews: {e}")
        return None



def perform_data_cleaning(df):

 # Perform data cleaning and transformation
        df['review_date'] = pd.to_datetime(df['at'])
        df = df.sort_values('review_date', ascending=False)
        df = df[['reviewId', 'userName', 'content', 'score', 'thumbsUpCount','reviewCreatedVersion','review_date','appVersion']]



def save_app_reviews(df, output_dir='data'):
    """
    Saves the app reviews to a CSV file.

    Args:
        df (pandas.DataFrame): The DataFrame containing the app reviews.
        output_dir (str, optional): The directory to save the output CSV file. Defaults to 'data'.
    """
    output_file = f'apollo_reviews_{pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")}.csv'
    output_path = os.path.join(output_dir, output_file)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Save DataFrame as a CSV file
        df.to_csv(output_path, index=False)
        print(f"App reviews saved to: {output_path}")
    except Exception as e:
        print(f"Error occurred while saving app reviews: {e}")