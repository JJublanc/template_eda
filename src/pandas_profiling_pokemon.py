from pandas_profiling import ProfileReport
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('./data/Pokemon.csv')
    profile = ProfileReport(df[0:100], title="Report")
    profile.to_file("./reports/pokemon_pandas_profiling.html")