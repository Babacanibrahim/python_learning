import numpy as np
import pandas as pd

dataset = {
        "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
        "Çalışan": ["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
        "Maaş":[3000,3500,2500,4500,4000,2000]
        }

df = pd.DataFrame(dataset)
print(df)

print(int(df.groupby("Departman")["Maaş"].sum().loc["Bilişim"]))

print((df.groupby("Departman")["Çalışan"].count()))

print(df.groupby("Departman").max())

print(df.groupby("Departman")["Maaş"].min()["Bilişim"])

print(df.groupby("Departman")["Maaş"].mean())
