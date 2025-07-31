import pandas as pd
import numpy as np

arr = [[10,20,np.nan],[np.nan,50,60],[70,np.nan,np.nan]]

df = pd.DataFrame(arr, index=["A","B","C"],columns=["C1","C2,","C3"])

# df.dropna(inplace=True)
print(df)

# print(df.sum().sum())
# print(df.size)
# print(pd.isnull(df).sum().sum())

def calculateMean(df):
    total = df.sum().sum()
    size = df.size - pd.isnull(df).sum().sum()

    mean = total/size
    return mean

mean = calculateMean(df)

df.fillna(value=mean, inplace=True)

print(df)
