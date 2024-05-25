import pandas as pd
import unittest
from datetime import datetime

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
    
        self.data = {
            'reviewId': [1, 2, 3, 4, 5],
            'userName': ['User1', 'User2', 'User3', 'User4', 'User5'],
            'content': ['Great app!', 'Disappointing', 'Useful feature', 'Could be better', 'Awesome!'],
            'score': [5, 2, 4, 3, 5],
            'thumbsUpCount': [10, 3, 7, 5, 12],
            'reviewCreatedVersion': ['1.0.0', '2.1.0', None, '3.2.0', '1.5.0'],
            'at': ['2022-01-01', '2021-12-15', '2022-03-10', '2021-11-30', '2022-02-20']
        }
        self.df = pd.DataFrame(self.data)

    def test_convert_to_datetime(self):
        df = convert_to_datetime(self.df, 'at')
        self.assertIsInstance(df['review_date'][0], pd.Timestamp)
        self.assertEqual(df['review_date'][0], pd.Timestamp('2022-01-01'))

    def test_sort_by_review_date(self):
        df = convert_to_datetime(self.df, 'at')
        sorted_df = sort_by_review_date(df)
        self.assertEqual(sorted_df['review_date'].tolist(), sorted([pd.Timestamp('2021-11-30'), pd.Timestamp('2021-12-15'), pd.Timestamp('2022-01-01'), pd.Timestamp('2022-02-20'), pd.Timestamp('2022-03-10')], reverse=True))

    def test_select_columns(self):
        df = select_columns(self.df, ['reviewId', 'userName', 'content'])
        self.assertEqual(list(df.columns), ['reviewId', 'userName', 'content'])

    def test_drop_nan_values(self):
        df = convert_to_datetime(self.df, 'at')
        cleaned_df = drop_nan_values(df, ['reviewCreatedVersion', 'appVersion'])
        self.assertEqual(len(cleaned_df), 4)

    def test_perform_data_cleaning(self):
        cleaned_df = perform_data_cleaning(self.df)
        self.assertEqual(list(cleaned_df.columns), ['reviewId', 'userName', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion', 'review_date', 'appVersion'])
        self.assertEqual(len(cleaned_df), 4)
        self.assertIsInstance(cleaned_df['review_date'][0], pd.Timestamp)

if __name__ == '__main__':
    unittest.main()