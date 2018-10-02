import pandas as pd
import numpy
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

importPath = "./datasets/US_Income_Kaggle.csv"

#IMPORT DATASET
df = pd.read_csv(importPath, encoding="ISO-8859-1 ", header=None)
# print(df.head(5))

# MARK ZERO VALUES AS MISSING OR NAN
# df[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]] = df[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]].replace(0, numpy.NaN)
# print(df.isnull().sum())

# exportPath = "./datasets/processed_income.csv"
# df.to_csv(exportPath)