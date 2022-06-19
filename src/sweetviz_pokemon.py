import sweetviz as sv
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('./data/Pokemon.csv')
    my_report = sv.analyze(df)
    my_report.show_html('./reports/sweetviz_pokemon.html') # Default arguments will generate to "SWEETVIZ_REPORT.html"


    # compare two datasets
    df_1 = df[:458]
    df_2 = df[458:]
    my_report = sv.compare([df_1, "Training Data"], [df_2, "Test Data"],"Speed")
    my_report.show_html('./reports/sweetviz_pokemon_comparison.html')