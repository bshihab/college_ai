import pandas as pd
from langchain.retrievers import BaseRetriever

class CSVRetriever(BaseRetriever):
    def __init__(self, df):
        self.df = df

    def retrieve(self, query):
        # Simple example: search for the query in the 'institution' column
        results = self.df[self.df['institution'].str.contains(query, case=False)]
        return results[['institution', 'world_rank', 'country']]

# Load the dataset
df = pd.read_csv('../data/college_test_data.csv')
retriever = CSVRetriever(df)