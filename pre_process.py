import pandas as pd
import numpy

importPath = "./datasets/US_Income_Kaggle.csv"

############ IMPORT DATASET ######################
df = pd.read_csv(importPath, encoding="ISO-8859-1 ")
# print(df.head(5))


################ CHECK MISSING DATA ################
# mark 0 values as missing or NaN
# df[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]] = df[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]].replace(0, numpy.NaN)
# print(df.isnull().sum())


################# BINNING ###########################
minMeanInt = int(min(df["Mean"]))
maxMeanInt = int(max(df["Mean"]))

binwidth = int((max(df["Mean"])-min(df["Mean"]))/4)
bins = [minMeanInt, minMeanInt + binwidth, maxMeanInt - binwidth, maxMeanInt]

group_names = ['Low', 'Medium', 'High']

df['Mean-Binned'] = pd.cut(df['Mean'], bins, labels=group_names)

# exportPath = "./datasets/processed_income.csv"
# df.to_csv(exportPath)