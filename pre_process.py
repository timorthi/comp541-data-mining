import pandas as pd
import numpy
import matplotlib.pyplot as plt

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
minMedianInt = int(min(df["Median"]))
maxMedianInt = int(max(df["Median"]))

meanBinwidth = int((max(df["Mean"])-min(df["Mean"]))/4)
meanBins = [minMeanInt, minMeanInt + meanBinwidth, maxMeanInt - meanBinwidth, maxMeanInt]

medianBinwidth = int((max(df["Median"])-min(df["Median"]))/4)
medianBins = [minMedianInt, minMedianInt + medianBinwidth, maxMedianInt - medianBinwidth, maxMedianInt]

group_names = ['Low', 'Medium', 'High']

df['Mean-Binned'] = pd.cut(df['Mean'], meanBins, labels=group_names)
df['Median-Binned'] = pd.cut(df['Median'], medianBins, labels=group_names)


# # plot histogram
# _ = plt.hist(df['Median'], bins=medianBins)
# _ = plt.xlabel('Median Income')
# _ = plt.ylabel('Number of Cities')
# plt.show()

# exportPath = "./datasets/processed_income.csv"
# df.to_csv(exportPath)