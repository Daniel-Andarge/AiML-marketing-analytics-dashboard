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
    Performs Univariate Analysis on the specified categorical features of a dataset.
    
    Args:
    df (pandas.DataFrame): The input dataset.
    columns (list): A list of column names to perform the analysis on.
    
    Returns:
    pandas.DataFrame: A DataFrame where the index are the column names and the columns are the unique values
                      and their corresponding frequency counts.
    """

    freq_counts_df = pd.DataFrame()

    for col in columns:


        freq_counts_df[col] = value_counts
    
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
 
    df['content'] = df['content'].str.lower().str.replace(r'[^\w\s]+', '')


    df['sentiment'] = df['content'].apply(lambda x: 'Positive' if TextBlob(x).sentiment.polarity > 0 else
                                         'Negative' if TextBlob(x).sentiment.polarity < 0 else 'Neutral')

    df['keywords'] = df['content'].apply(lambda x: ', '.join([word for word, count in Counter(str(x).split()).most_common(5)]))

    return df