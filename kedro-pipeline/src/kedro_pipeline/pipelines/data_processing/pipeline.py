"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.13
"""
from .nodes import perform_review_cleaning
from kedro.pipeline import Pipeline, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([])




output_path = perform_review_cleaning(raw_review_df, date_column='at', columns=['reviewId', 'userName', 'content', 'score', 'thumbsUpCount', 
                                                                                'reviewCreatedVersion', 'review_date', 'appVersion'], nan_columns=['reviewCreatedVersion', 'appVersion'])