import pandas as pd
import numpy as np
"""
# AXİS 0
dataset1 = {
    "A": ["A1","A2","A3","A4"],
    "B":["B1","B2","B3","B4"],
    "C":["C1","C2","C3","C4"],
}

dataset2 = {
    "A": ["A5","A6","A7","A8"],
    "B":["B5","B6","B7","B8"],
    "C":["C5","C6","C7","C8"],
}

df1 = pd.DataFrame(dataset1,index = [1,2,3,4])
df2 = pd.DataFrame(dataset2,index = [5,6,7,8] )

concat = pd.concat([df1,df2])
print(df1)
print(df2)
print(concat)

# AXİS 1
dataset3 = {
    "A": ["A1","A2","A3","A4"],
    "B":["B1","B2","B3","B4"],
    "C":["C1","C2","C3","C4"],
}

dataset4 = {
    "D": ["D1","D2","D3","D4"],
    "E":["E1","E2","E3","E4"],
    "F":["F1","F2","F3","F4"],
}

df3 = pd.DataFrame(dataset3,index = [1,2,3,4])
df4 = pd.DataFrame(dataset4,index = [1,2,3,4] )

concat2 = pd.concat([df3,df4], axis=1)
print(concat2)
"""

# MERGE
"""
dataset1 = {
    "A" : ["A1","A2","A3"],
    "B" : ["B1","B2","B3"],
    "anahtar" : ["K1","K2","K3"]
}

df1 = pd.DataFrame(dataset1,index = [1,2,3])

print(df1)

dataset2 = {
    "X" : ["X1","X2","X3","X4"],
    "Y" : ["Y1","Y2","Y3","Y4"],
    "anahtar" : ["K1","K2","K5","K4"]
}

df2 = pd.DataFrame(dataset2,index = [1,2,3,4])

print(df2)

print(pd.merge(df1,df2,how="inner",on="anahtar"))"""

# JOİN
dataset1 = {
    "A" : ["A1","A2","A3","A4"],
    "B" : ["B1","B2","B3","A4"],
}
dataset2 = {
    "X" : ["X1","X2","X3"],
    "Y" : ["Y1","Y2","Y3"],
    
}

df1 = pd.DataFrame(dataset1,index = [1,2,3,4]) 
df2 = pd.DataFrame(dataset2,index = [1,2,3])

print(df1)
print(df2)

print(df1.join(df2))
print(df2.join(df1))