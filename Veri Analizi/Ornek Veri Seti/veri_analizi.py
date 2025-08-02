import pandas as pd

df = pd.read_csv("mls-salaries-2017.csv")

# print(df)

# first_ten = (df.head(n = 10))

# indexes_count = (len(df.index))

# mean_salary = ((sum(df["base_salary"]))/indexes_count)

# print(df["base_salary"].max())

en_yukesk_tzminat = df[df["guaranteed_compensation"].max()== df["guaranteed_compensation"]]

gonzalez_pirez_mevki = df[(df["last_name"] =="Gonzalez Pirez")]["position"].iloc[0]

ortalama_mevki_maasi = df.groupby("position")["guaranteed_compensation"].mean()

farkli_mevkiler = df["position"].nunique()

mevkideki_oyuncular = df["position"].value_counts()

takimdaki_oyuncular = df["club"].value_counts()

def re_find(last_name):
    if "son" in last_name:
        return True
    return False

soyadinda_son_gecen = df[df["last_name"].apply(re_find)]

print(soyadinda_son_gecen)