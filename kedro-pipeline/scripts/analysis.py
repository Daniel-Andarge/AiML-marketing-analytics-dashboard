import pandas as pd

def univariate_analysis(df):
    """
    Performs Univariate Analysis on the numerical features of a dataset.
    
    Args:
    df (pandas.DataFrame): The input dataset.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the descriptive statistics for the numerical features.
    """
    
    # Create a dictionary to store the descriptive statistics
    stats = {}
    
    # Iterate through the numerical features
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        # Calculate the descriptive statistics
        mean = df[col].mean()
        median = df[col].median()
        mode = df[col].mode()[0]
        std_dev = df[col].std()
        min_val = df[col].min()
        max_val = df[col].max()
        
        # Store the statistics in the dictionary
        stats[col] = {
            'Mean': mean,
            'Median': median,
            'Mode': mode,
            'Standard Deviation': std_dev,
            'Minimum': min_val,
            'Maximum': max_val
        }
    
    # Convert the dictionary to a pandas DataFrame
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
    
    # Create an empty DataFrame to store the results
    freq_counts_df = pd.DataFrame()
    
    # Iterate through the specified columns
    for col in columns:
        # Get the frequency counts for the unique values in the column
        value_counts = df[col].value_counts()
        
        # Add the frequency counts to the DataFrame
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


