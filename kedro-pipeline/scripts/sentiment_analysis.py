import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.graph_objects as go

def get_key_strengths_and_weaknesses(reviews):
    """
    Identify the key strengths and weaknesses from the review sentiment data.
    
    Args:
        reviews (pandas.DataFrame): A DataFrame containing the review data with columns 'content' and 'sentiment_score'.
    
    Returns:
        None
    """
    # Group the sentiment scores by the review text and calculate the average sentiment score for each review
    reviews_by_sentiment = reviews.groupby('content')['sentiment_score'].mean().sort_values(ascending=False)
    
    # Identify the top and bottom reviews
    top_reviews = reviews_by_sentiment.head(10)
    bottom_reviews = reviews_by_sentiment.tail(10)
    
    # Visualize the common keywords in top and bottom reviews
    top_text = ' '.join(reviews[reviews['content'].isin(top_reviews.index)]['content'])
    bottom_text = ' '.join(reviews[reviews['content'].isin(bottom_reviews.index)]['content'])
    
    top_wordcloud = WordCloud(width=1600, height=800).generate(top_text)
    bottom_wordcloud = WordCloud(width=1600, height=800).generate(bottom_text)
    
    plt.figure(figsize=(30, 15))
    plt.subplot(1, 2, 1)
    plt.imshow(top_wordcloud)
    plt.title('Key Strengths')
    plt.subplot(1, 2, 2)
    plt.imshow(bottom_wordcloud)
    plt.title('Key Weaknesses')
    plt.show()

def get_sentiment_across_time(reviews):
    """
    Analyze the general sentiment across time.
    
    Args:
        reviews (pandas.DataFrame): A DataFrame containing the review data with columns 'review_date' and 'sentiment_score'.
    
    Returns:
        None
    """
    reviews['review_date'] = pd.to_datetime(reviews['review_date'])
    reviews['week'] = reviews['review_date'].dt.isocalendar().week
    sentiment_by_week = reviews.groupby('week')['sentiment_score'].mean()
    sentiment_by_week.plot()
    plt.title('Sentiment Across Time')
    plt.xlabel('Week')
    plt.ylabel('Average Sentiment Score')
    plt.show()

def get_sentiment_and_version_updates(reviews):
    """
    Analyze the relationship between sentiment and version updates.
    
    Args:
        reviews (pandas.DataFrame): A DataFrame containing the review data with columns 'review_date', 'appVersion', and 'sentiment_score'.
    
    Returns:
        None
    """
    reviews['version_sentiment'] = reviews.groupby(['appVersion', pd.Grouper(key='review_date', freq='W')])['sentiment_score'].transform('mean')

    # Create the Plotly line plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=reviews['review_date'], y=reviews['version_sentiment'], mode='lines'))
    fig.update_layout(
        title='Sentiment and Version Updates',
        xaxis_title='Date',
        yaxis_title='Average Sentiment Score',
        width=800,
        height=600
    )
    fig.show()