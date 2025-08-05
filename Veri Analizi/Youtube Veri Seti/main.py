import pandas as pd

df = pd.read_csv("USvideos.csv")

"""
ilk_bes_veri = df.head(n = 5)

print(ilk_bes_veri)
"""

df.drop(columns=["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"], inplace=True)

"""
# columns = len(df.columns)
# rows  = len(df.index)
# print(columns)
# print(rows)
"""

"""
ortalama_begeni = df["likes"].mean()
ortlama_begenmeme = df["dislikes"].mean()
print(ortalama_begeni)
print(ortlama_begenmeme)
"""

"""
max_views = df[df["views"] == df["views"].max()]["title"].iloc[0]
min_views = df[df["views"] == df["views"].min()]["title"].iloc[0]
print(min_views)
print(max_views)
"""

"""
categories = df.groupby("category_id")

print(categories["comment_count"].mean())

print(df["category_id"].value_counts())
"""

"""
def countTitleCount(title):
    return len(title)

df["title_length"] = df["title"].apply(countTitleCount)

print(df)

def countTag(tags):
    tagList = tags.split("|")
    return len(tagList)

df["title_length"] = df["tags"].apply(countTag)
"""
