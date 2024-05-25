import pandas as pd

from textblob import TextBlob
from collections import Counter
def univariate_analysis(df):
    """
    Performs Univariate Analysis on the numerical features of a dataset.
    
    Args:
    df (pandas.DataFrame): The input dataset.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the descriptive statistics for the numerical features.
    """

    stats = {}

    for col in df.select_dtypes(include=['int64', 'float64']).columns:
     
        mean = df[col].mean()
        median = df[col].median()
        mode = df[col].mode()[0]
        std_dev = df[col].std()
        min_val = df[col].min()
        max_val = df[col].max()
        
   
        stats[col] = {
            'Mean': mean,
            'Median': median,
            'Mode': mode,
            'Standard Deviation': std_dev,
            'Minimum': min_val,
            'Maximum': max_val
        }
    
    stats_df = pd.DataFrame.from_dict(stats, orient='index')
    
    return stats_df




def categorical_univariate_analysis(df, columns):
    """
    Perform categorical univariate analysis on the given DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    columns (list): List of column names to perform the analysis on.

    Returns:
    pandas.DataFrame: A DataFrame containing the frequency counts for each column.
    """
    freq_counts_df = pd.DataFrame()

    for col in columns:
        freq_counts_df[col] = df[col].value_counts()

    return freq_counts_df




def describe_telegram_subscribers(df):
    """
    Calculates the descriptive statistics for the Telegram subscribers dataset.
    
    Parameters:
    df (pandas.DataFrame): A DataFrame containing the following columns:
        - 'date': The date of the subscriber count.
        - 'total_subscribers': The total number of subscribers.
        - 'daily_subscribers': The daily change in the number of subscribers.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the descriptive statistics for the 'total_subscribers' and 'daily_subscribers' columns.
    """
    stats = df[['daily_subscribers']].describe()
    
    return stats


def sentiment_analysis(df):
    # Clean the 'content' column
    df['content'] = df['content'].str.lower().str.replace(r'[^\w\s]+', '')

    # Perform sentiment analysis
    df['sentiment_score'] = df['content'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Assign sentiment label based on sentiment score
    df['sentiment'] = df['sentiment_score'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')

    # Extract the top 5 keywords
    df['keywords'] = df['content'].apply(lambda x: ', '.join([word for word, count in Counter(str(x).split()).most_common(5)]))

    return df


import pandas as pd

def calculate_ad_performance(df):
    """
    Calculates ad performance metrics for a given dataset.
    
    Parameters:
    df (pandas.DataFrame): The input dataset containing the necessary columns.
    
    Returns:
    pandas.DataFrame: The updated dataset with the new performance metrics.
    """

    df['ad_id'] = df['bank'] + '_' + df['post_link']
    
    df['impressions'] = df['views']
    df['engagement_rate'] = 1.0  
    
    return df