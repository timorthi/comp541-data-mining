# Make sure you download the CSV version of the dataset
# Process:
## Drop the following collumn from the start:
## DR Number, Mo Code, Victim Age
## Status Description, Premise Description, Area Name, Location
## Weapon Description
##
## Add following column:
## Violent crime (boolean, 0 is no violence, 1 is violence)
##

## Note: Later revisions may require adjustments to this script

import pandas as pd

print("Opening LA Crime dataset")
DATASET_PATH = "../datasets/Crime_Data_from_2010_to_Present.csv"
DATASET_PROCESSED_PATH = "../datasets/Crime_Data_from_2010_to_Present_processed.csv"
df = pd.read_csv(DATASET_PATH)

print("Removing unwanted columns")
# Drop some of the unneeded fields
unneeded_columns = ["DR Number", "MO Codes", "Victim Age", "Status Description", 
"Premise Description", "Area Name", "Location ", "Weapon Description", "Crime Code Description"]
df.drop(columns=unneeded_columns, inplace=True) 

print("Creating and updating Violence column")
# Create Violence row, init to 0
df["Violence"] = 0

# Use loc to make a sheet-wide modification
# This will make "Violence" 1 for any "Weapon Used Code" field that's not nan
# Pandas is really fast at doing this!
df.loc[df["Weapon Used Code"] == df["Weapon Used Code"], "Violence"] = 1
    
print("Saving")    
# Save this
df.to_csv(DATASET_PROCESSED_PATH, encoding="utf-8", index=False)














