import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_unique_posts_per_bank(df):
    """
    Plots a bar chart showing the number of unique posts per bank using Plotly.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame with the bank and post count information.
    """
    fig = go.Figure(data=[go.Bar(
        x=df['bank'],
        y=df['count'],
        textposition='auto'
    )])

    fig.update_layout(
        title='Number of Unique Posts per Bank',
        xaxis_title='Bank',
        yaxis_title='Number of Unique Posts',
        xaxis_tickangle=-45
    )

    fig.show()



def scatter_plot(df, x_col, y_col):
    """
    Plot the relationship between two columns in the given DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    x_col (str): The name of the column to use for the x-axis.
    y_col (str): The name of the column to use for the y-axis.
    """
    
    fig = go.Figure(data=go.Scatter(
        x=df[x_col],
        y=df[y_col],
        mode='markers'
    ))
    
    fig.update_layout(
        title=f"Relationship between {x_col} and {y_col}",
        xaxis_title=x_col,
        yaxis_title=y_col,
        width=800,
        height=600
    )
    
    pio.show(fig)



def descriptive_stats(df):
    """
    Calculates the descriptive statistics and creates histograms for the numerical features in the provided DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    """
    # Calculate the descriptive statistics
    score_stats = {
        'Mean': df['score'].mean(),
        'Median': df['score'].median(),
        'Mode': df['score'].mode()[0],
        'Standard Deviation': df['score'].std(),
        'Minimum': df['score'].min(),
        'Maximum': df['score'].max()
    }

    thumbsUpCount_stats = {
        'Mean': df['thumbsUpCount'].mean(),
        'Median': df['thumbsUpCount'].median(),
        'Mode': df['thumbsUpCount'].mode()[0],
        'Standard Deviation': df['thumbsUpCount'].std(),
        'Minimum': df['thumbsUpCount'].min(),
        'Maximum': df['thumbsUpCount'].max()
    }

    # Create histograms
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Histogram for 'score'
    ax1.hist(df['score'], bins=10, density=True)
    ax1.set_title('Distribution of Score')
    ax1.set_xlabel('Score')
    ax1.set_ylabel('Probability')

    # Histogram for 'thumbsUpCount'
    ax2.hist(df['thumbsUpCount'], bins=10, density=True)
    ax2.set_title('Distribution of Thumbs Up Count')
    ax2.set_xlabel('Thumbs Up Count')
    ax2.set_ylabel('Probability')

    plt.show()



def visualize_descriptive_stats(df):
    """
    Calculates the descriptive statistics and creates histograms for the numerical features in the provided DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    """
    # Calculate the descriptive statistics
    score_stats = {
        'Mean': df['score'].mean(),
        'Median': df['score'].median(),
        'Mode': df['score'].mode()[0],
        'Standard Deviation': df['score'].std(),
        'Minimum': df['score'].min(),
        'Maximum': df['score'].max()
    }

    thumbsUpCount_stats = {
        'Mean': df['thumbsUpCount'].mean(),
        'Median': df['thumbsUpCount'].median(),
        'Mode': df['thumbsUpCount'].mode()[0],
        'Standard Deviation': df['thumbsUpCount'].std(),
        'Minimum': df['thumbsUpCount'].min(),
        'Maximum': df['thumbsUpCount'].max()
    }

    print('Descriptive Statistics:')
    print('score:')
    for key, value in score_stats.items():
        print(f'{key}: {value:.6f}')
    print('\nthumbsUpCount:')
    for key, value in thumbsUpCount_stats.items():
        print(f'{key}: {value:.6f}')

    # Create histograms
    fig = go.Figure()

    # Histogram for 'score'
    fig.add_trace(go.Histogram(x=df['score'], nbinsx=10, histnorm='probability', name='Score'))
    fig.update_layout(
        title='Distribution of Score',
        xaxis_title='Score',
        yaxis_title='Probability'
    )

    # Histogram for 'thumbsUpCount'
    fig.add_trace(go.Histogram(x=df['thumbsUpCount'], nbinsx=10, histnorm='probability', name='Thumbs Up Count'))
    fig.update_layout(
        title='Distribution of Thumbs Up Count',
        xaxis_title='Thumbs Up Count',
        yaxis_title='Probability'
    )

    fig.show()



def analyze_review_trends(df):
    """
    Analyze the trends in review scores and thumbs up count over time using Plotly.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the review data.
    """
    # Convert the 'review_date' column to datetime
    df['review_date'] = pd.to_datetime(df['review_date'])

    # Group the data by review date and calculate aggregations
    review_trends = df.groupby(pd.Grouper(key='review_date', freq='D')).agg({
        'score': 'mean',
        'thumbsUpCount': 'sum',
        'content': 'count'
    }).reset_index()

    # Create the Plotly figure
    fig = go.Figure()

    # Add the review score trend
    fig.add_trace(
        go.Scatter(x=review_trends['review_date'], y=review_trends['score'], mode='lines', name='Average Score')
    )

    # Add the thumbs up count trend
    fig.add_trace(
        go.Scatter(x=review_trends['review_date'], y=review_trends['thumbsUpCount'], mode='lines', name='Total Thumbs Up')
    )

    # Update the layout
    fig.update_layout(
        title='Trends in Review Scores and Thumbs Up Count Over Time',
        xaxis_title='Review Date',
        yaxis_title='Average Score',
        yaxis2=dict(
            title='Total Thumbs Up',
            overlaying='y',
            side='right'
        )
    )

    fig.show()




def categorical_frequency_plot(df):
    """
    Create a bar plot to display the frequency of each category in the DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    """
    
    # Convert 'reviewCreatedVersion' to datetime objects
    df['reviewCreatedVersion'] = pd.to_datetime(df['reviewCreatedVersion'], format='%y.%m.%d')
    
    # Extract year, month, and day components
    df['Year'] = df['reviewCreatedVersion'].dt.year.astype(str)
    df['Month'] = df['reviewCreatedVersion'].dt.month.astype(str)
    df['Day'] = df['reviewCreatedVersion'].dt.day.astype(str)
    
    # Create the bar plot
    fig = go.Figure(data=[go.Bar(
        x=df['Year'] + '.' + df['Month'] + '.' + df['Day'],
        y=df['appVersion']
    )])
    
    fig.update_layout(
        title='Frequency Plot',
        xaxis_title='reviewCreatedVersion',
        yaxis_title='Frequency',
        bargap=0.1
    )
    
    fig.show()


def visualize_categorical_univariate_analysis(freq_counts_df):
    """
    Visualizes the output of the categorical_univariate_analysis() function.
    
    Args:
    freq_counts_df (pandas.DataFrame): The output DataFrame from categorical_univariate_analysis().
    """
    
    # Create a Plotly figure
    fig = go.Figure()
    
    # Iterate through the columns in the DataFrame
    for col in freq_counts_df.columns:
        # Create a bar trace for each column
        fig.add_trace(go.Bar(
            x=freq_counts_df.index,
            y=freq_counts_df[col],
            name=col
        ))
    
    fig.update_layout(
        title='Frequency of the App Version',
        xaxis_title='Unique Values',
        yaxis_title='Frequency Counts',
        barmode='group',
        bargap=0.1
    )
    
    fig.show()




def plot_telegram_subscribers(df):
    """
    Plots a time series plot for Telegram subscribers.
    
    Parameters:
    df (pandas.DataFrame): A DataFrame containing the following columns:
        - 'date': The date of the subscriber count.
        - 'total_subscribers': The total number of subscribers.
        - 'daily_subscribers': The daily change in the number of subscribers.
    """
    # Convert the 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

    # Create the time series plot
    fig = go.Figure()

    # Add the total subscribers trace
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['total_subscribers'],
        mode='lines+markers',
        name='Total Subscribers'
    ))

    # Add the daily subscribers trace
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['daily_subscribers'],
        mode='lines+markers',
        name='Daily Subscribers'
    ))

    # Update the layout
    fig.update_layout(
        title='Bank of Abyssinia Telegram Subscribers Over Time',
        xaxis_title='Date',
        yaxis_title='Number of Subscribers',
        xaxis_type='date',
        xaxis_tickformat='%b %d, %Y'
    )

    # Display the plot
    fig.show()



def visualize_sentiment_analysis(df):
    """
    Visualize the sentiment analysis results from a given DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the sentiment analysis data.

    Returns:
    None
    """
    # Sentiment Category Distribution
    fig1 = px.bar(df['sentiment'].value_counts(), x=df['sentiment'].value_counts().index, y=df['sentiment'].value_counts(), title='Sentiment Category Distribution', width=800, height=600)
    fig1.update_layout(xaxis_title='Sentiment Category', yaxis_title='Count')
    fig1.show()

    # Sentiment Category Heatmap by Keyword
    sentiment_pivot = df.groupby(['keywords', 'sentiment']).size().unstack(fill_value=0)
    fig2 = go.Figure(data=go.Heatmap(
        x=sentiment_pivot.columns,
        y=sentiment_pivot.index,
        z=sentiment_pivot.values,
        colorscale='RdYlGn',
        zmin=-1, zmax=1,
        colorbar_title='Sentiment Score'
    ))
    fig2.update_layout(title='Sentiment Category Heatmap by Keyword', width=800, height=600, xaxis_title='Sentiment Category', yaxis_title='Keyword')
    fig2.show()

    # Sentiment Categories by Keyword
    sentiment_counts = df.groupby(['keywords', 'sentiment'])['sentiment'].count().unstack(fill_value=0)
    fig3 = px.bar(sentiment_counts, x=sentiment_counts.index, y=sentiment_counts.columns, title='Sentiment Categories by Keyword', width=1200, height=800)
    fig3.update_layout(xaxis_title='Keyword', yaxis_title='Count', legend_title='Sentiment Category')
    fig3.show()

def plot_ad_performance(df):
    """
    Creates a line plot visualization of the ad performance metrics.
    
    Parameters:
    df (pandas.DataFrame): The input dataset containing the ad performance metrics.
    """
    # Ensure the required columns are present in the DataFrame
    required_cols = ['bank', 'impressions', 'engagement_rate']
    if not all(col in df.columns for col in required_cols):
        raise ValueError("The DataFrame must contain the following columns: 'bank', 'impressions', 'engagement_rate'.")
    
    # Group the data by bank and calculate the mean performance metrics
    bank_performance = df.groupby('bank')[['impressions', 'engagement_rate']].mean().reset_index()
    
    # Create the line plot
    fig = go.Figure()
    
    # Add the impressions line
    fig.add_trace(go.Scatter(x=bank_performance['bank'], y=bank_performance['impressions'], mode='lines+markers', name='Impressions'))
    
    # Add the engagement rate line
    fig.add_trace(go.Scatter(x=bank_performance['bank'], y=bank_performance['engagement_rate'], mode='lines+markers', name='Engagement Rate'))
    
    # Customize the layout
    fig.update_layout(
        title='Ad Performance Metrics by Bank',
        xaxis_title='Bank',
        yaxis_title='Value',
        font=dict(family='Arial', size=14),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    
    fig.show()


def analyze_optimal_ad_placement(df):
    """
    Analyzes the optimal ad placement for banks based on the views per post.
    
    Parameters:
    df (pandas.DataFrame): The input dataset containing the bank data.
    
    Returns:
    None
    """
    # Ensure the required columns are present in the DataFrame
    required_cols = ['bank', 'views', 'time_of_day', 'post_link']
    if not all(col in df.columns for col in required_cols):
        raise ValueError("The DataFrame must contain the following columns: 'bank', 'views', 'time_of_day', 'post_link'.")
    
    # Find the bank with the highest average views per post
    bank_views = df.groupby('bank')['views'].mean().reset_index()
    top_bank = bank_views.loc[bank_views['views'].idxmax()]['bank']
    
    # Analyze the "time_of_day" distribution of the top-performing bank's ads
    top_bank_df = df[df['bank'] == top_bank]
    top_bank_time_dist = top_bank_df.groupby('time_of_day')['views'].mean().reset_index()
    
    # Analyze the "time_of_day" distribution of the other banks' ads
    other_banks_df = df[df['bank'] != top_bank]
    other_banks_time_dist = other_banks_df.groupby('time_of_day')['views'].mean().reset_index()
    
    # Visualize the views per post for each bank
    fig = go.Figure()
    fig.add_trace(go.Bar(x=bank_views['bank'], y=bank_views['views'], name='Views per Post'))
    fig.update_layout(
        title='Views per Post by Bank',
        xaxis_title='Bank',
        yaxis_title='Views per Post',
        font=dict(family='Arial', size=14)
    )
    fig.show()
    
    # Visualize the "time_of_day" distribution for the top-performing bank and other banks
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=top_bank_time_dist['time_of_day'], y=top_bank_time_dist['views'], mode='lines+markers', name=top_bank))
    fig.add_trace(go.Scatter(x=other_banks_time_dist['time_of_day'], y=other_banks_time_dist['views'], mode='lines+markers', name='Other Banks'))
    fig.update_layout(
        title='Time of Day Distribution of Views',
        xaxis_title='Time of Day',
        yaxis_title='Average Views',
        font=dict(family='Arial', size=14),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    fig.show()


def ad_per_time_of_day(df):
    """
    Analyzes the optimal ad placement for banks based on the views per post.
    
    Parameters:
    df (pandas.DataFrame): The input dataset containing the bank data.
    
    Returns:
    None
    """
    # Ensure the required columns are present in the DataFrame
    required_cols = ['bank', 'views', 'time_of_day', 'post_link']
    if not all(col in df.columns for col in required_cols):
        raise ValueError("The DataFrame must contain the following columns: 'bank', 'views', 'time_of_day', 'post_link'.")
    
    # Find the bank with the highest average views per post
    bank_views = df.groupby('bank')['views'].mean().reset_index()
    top_bank = bank_views.loc[bank_views['views'].idxmax()]['bank']
    
    # Analyze the "time_of_day" distribution of the top-performing bank's ads
    top_bank_df = df[df['bank'] == top_bank]
    top_bank_time_dist = top_bank_df.groupby('time_of_day')['post_link'].count().reset_index()
    top_bank_time_dist.columns = ['time_of_day', 'num_posts']
    
    # Analyze the "time_of_day" distribution of the other banks' ads
    other_banks_df = df[df['bank'] != top_bank]
    other_banks_time_dist = other_banks_df.groupby('time_of_day')['post_link'].count().reset_index()
    other_banks_time_dist.columns = ['time_of_day', 'num_posts']

    
    # Visualize the "time_of_day" distribution for the top-performing bank and other banks
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=top_bank_time_dist['time_of_day'], y=top_bank_time_dist['num_posts'], mode='lines+markers', name=top_bank))
    fig.add_trace(go.Scatter(x=other_banks_time_dist['time_of_day'], y=other_banks_time_dist['num_posts'], mode='lines+markers', name='Other Banks'))
    fig.update_layout(
        title='Number of Posts per Time of Day',
        xaxis_title='Time of Day',
        yaxis_title='Number of Posts',
        font=dict(family='Arial', size=14),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    fig.show()