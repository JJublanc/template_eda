from pandas_profiling import ProfileReport
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('./data/tweets/final_data.csv')
    profile = ProfileReport(df[0:100], title="Report")
    profile.to_file("./reports/tweets_pandas_profiling.html")