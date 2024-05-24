def convert_to_datetime(df, date_column):
    """
    Converts the specified date column in the dataframe to a datetime column.
    
    Args:
    df (pandas.DataFrame): The input dataframe.
    date_column (str): The name of the column to be converted to datetime.
    
    Returns:
    pandas.DataFrame: The dataframe with the specified column converted to datetime.
    """
    df['review_date'] = pd.to_datetime(df[date_column])
    return df

def sort_by_review_date(df, sort_column='review_date', ascending=False):
    """
    Sorts the dataframe in the specified order by the specified column.
    
    Args:
    df (pandas.DataFrame): The input dataframe.
    sort_column (str, optional): The name of the column to sort by. Defaults to 'review_date'.
    ascending (bool, optional): Whether to sort in ascending or descending order. Defaults to False (descending).
    
    Returns:
    pandas.DataFrame: The sorted dataframe.
    """
    df = df.sort_values(sort_column, ascending=ascending)
    return df

def select_columns(df, columns):
    """
    Selects the specified columns from the dataframe.
    
    Args:
    df (pandas.DataFrame): The input dataframe.
    columns (list): The list of column names to select.
    
    Returns:
    pandas.DataFrame: The dataframe with the selected columns.
    """
    df = df[columns]
    return df

def drop_nan_values(df, columns):
    """
    Drops rows with NaN values in the specified columns.
    
    Args:
    df (pandas.DataFrame): The input dataframe.
    columns (list): The list of column names to check for NaN values.
    
    Returns:
    pandas.DataFrame: The dataframe with rows containing NaN values in the specified columns removed.
    """
    df = df.dropna(subset=columns)
    return df

def perform_data_cleaning(df, date_column='at', sort_column='review_date'):
    """
    Performs the complete data cleaning process by calling the above functions.
    
    Args:
    df (pandas.DataFrame): The input dataframe.
    date_column (str, optional): The name of the column to be converted to datetime. Defaults to 'at'.
  
    Returns:
    pandas.DataFrame: The cleaned dataframe.
    """

    columns=['reviewId', 'userName', 'content', 'score', 'thumbsUpCount', 
              'reviewCreatedVersion', 'review_date', 'appVersion']
    
    nan_columns=['reviewCreatedVersion', 'appVersion']
    df = convert_to_datetime(df, date_column)
    df = sort_by_review_date(df, sort_column)
    df = select_columns(df, columns)
    df = drop_nan_values(df, nan_columns)
    
    return df