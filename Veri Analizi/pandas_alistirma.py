import pandas as pd
import numpy as np
from numpy.random import randn
"""

arr = randn(3, 3)

df = pd.DataFrame(data=arr, index=["A", "B", "C"], columns=["SÜTUN1", "SÜTUN2", "SÜTUN3"])

print(df)
print("********************")
#print(df[df["SÜTUN1"]>0])

print(df.loc["A"])"""


# MULTI INDEX

outerIndex = ["Grup1","Grup1","Grup1","Grup2","Grup2","Grup2","Grup3","Grup3","Grup3"]
innerInnex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]


liste = list(zip(outerIndex, innerInnex))


multiIndex = pd.MultiIndex.from_tuples(liste)


df = pd.DataFrame(randn(9, 3), index=multiIndex, columns=["A", "B", "C"])

df.index.names = ["Groups","Indexes"]

print(df)

print(df.xs("Index1",level="Indexes"))
