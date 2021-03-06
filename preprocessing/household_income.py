import pandas as pd
import numpy
# import matplotlib.pyplot as plt

importPath = "../datasets/US_Income_Kaggle.csv"
outputPath = "../datasets/us_income_kaggle_processed.csv"

############ IMPORT DATASET ######################
print('Loading file...')
df = pd.read_csv(importPath, encoding="ISO-8859-1 ")


################ CHECK MISSING DATA ################
# mark 0 values as missing or NaN
# df[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]] = df[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]].replace(0, numpy.NaN)
# print(df.isnull().sum())


print('Begin processing file')
################# BINNING ###########################
minMeanInt = int(min(df["Mean"]))
maxMeanInt = int(max(df["Mean"]))
minMedianInt = int(min(df["Median"]))
maxMedianInt = int(max(df["Median"]))

meanBinwidth = int((max(df["Mean"])-min(df["Mean"]))/4)
meanBins = [minMeanInt, minMeanInt + meanBinwidth, maxMeanInt - meanBinwidth, maxMeanInt]

medianBinwidth = int((max(df["Median"])-min(df["Median"]))/4)
medianBins = [minMedianInt, minMedianInt + medianBinwidth, maxMedianInt - medianBinwidth, maxMedianInt]

mean_group_names = ['MeanLow', 'MeanMedium', 'MeanHigh']
median_group_names = ['MedianLow', 'MedianMedium', 'MedianHigh']

df['Mean-Binned'] = pd.cut(df['Mean'], meanBins, labels=mean_group_names)
df['Median-Binned'] = pd.cut(df['Median'], medianBins, labels=median_group_names)


# # plot histogram
# _ = plt.hist(df['Median'], bins=medianBins)
# _ = plt.xlabel('Median Income')
# _ = plt.ylabel('Number of Cities')
# plt.show()

#################### Z-SCORE #######################

df["Mean"] = (df["Mean"] - df["Mean"].mean())/df["Mean"].std()
df["Median"] = (df["Median"] - df["Median"].mean())/df["Median"].std()

############## ATTRIBUTE CONSTRUCTION ##############

mean_dummy = pd.get_dummies(df['Mean-Binned'])
median_dummy = pd.get_dummies(df['Median-Binned'])

df = pd.concat([df, mean_dummy], axis=1)
df = pd.concat([df, median_dummy], axis=1)

################### DATA REDUCTION ##################

df.drop(['id', 'State_Code', 'State_Name', 'County', 'Place', 'Type', 'Primary', 'ALand', 'AWater'], axis=1, inplace=True)

########## EXPORT PRE-PROCESSED DATASET ############
df.to_csv(outputPath)
print(f'Saved to {outputPath}')
