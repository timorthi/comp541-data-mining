# Here's a short intro to loading a dataset into python and doing some sort of processing on it

from pathlib import Path
import pandas as pd

# In this example I'm going to work with my CSV dataset located in "datasets.sample/us_household_income.csv", so let's
# set some constants that represent some relevant paths. All uppercase variables represent constants in Python,
# even though they technically are mutable variables.
PROJECT_ROOT_PATH = Path(__file__).resolve().parents[1]
DATASET_PATH = PROJECT_ROOT_PATH.joinpath('datasets.sample/us_household_income.csv')

# Using pandas' read_csv method to load the file into a pandas.DataFrame object
df = pd.read_csv(DATASET_PATH, encoding='ISO-8859-1') # Pandas failed to load with utf-8 encoding, so setting it to ISO-8859-1 seems to do the trick.

print('*** Preview the DataFrame using DataFrame.head() ***')
print(df.head(), end='\n\n\n')

# This dataset has a few columns that we don't need for this project, like `State_Code`, so I'm going
# to tell pandas to drop those columns from my DataFrame.
unneeded_columns = ['id', 'State_Code', 'Primary', 'Place', 'Type']
print(f'*** Removing columns {unneeded_columns} ***')
df.drop(columns=unneeded_columns, inplace=True) # inplace=True to modify df itself instead of returning a copy
print('*** Finished removing columns ***', end='\n\n\n')

print('*** Preview the DataFrame again, noting that for each row, the columns in `unneeded_columns` are now gone')
print(df.head(), end='\n\n\n')

# Let's pretend we're doing some more processing here

# We're done processing this dataset, so let's export this DataFrame into a csv again
PROCESSED_FILE_PATH = PROJECT_ROOT_PATH.joinpath('datasets.sample/us_household_income_processed.csv')
df.to_csv(PROCESSED_FILE_PATH, encoding='utf-8', index=False) # index=False because DataFrames have an index (like an array) but we don't need to export that to a csv.
# Done! You should see a us_household_income_processed.csv in datasets.sample/ which contains the updated values.

# Next steps: for a more in-depth tutorial see https://realpython.com/python-data-cleaning-numpy-pandas/
# Our dataset is clean enough that I think pandas can handle all of it, so for example if you want to clean null values,
# just google "pandas remove null" and I'm sure you'll be pointed in the right direction from there :)
