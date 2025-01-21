import pandas as pd

# Placeholder for accessing the DataFrame
# Assuming Main.getter() returns the relevant DataFrame(s)
from processing.display import Main

def inspect_dataframe():
    with Main() as bot:
        bot.main_()
        # Retrieve the DataFrame(s) from Main.getter()
        new_df, movies, movies2 = bot.getter()

        # Print details about new_df
        print("---- new_df Columns ----")
        print(new_df.columns)
        print("\n---- new_df Info ----")
        print(new_df.info())

        print("\n---- new_df Sample Data ----")
        print(new_df.head())

        # Similarly, print details about other DataFrames if needed
        print("\n---- movies Columns ----")
        print(movies.columns)
        print("\n---- movies Sample Data ----")
        print(movies.head())

if __name__ == "__main__":
    inspect_dataframe()
