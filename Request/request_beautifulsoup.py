import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)

html_icerigi=response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

names=[]
for i in soup.find_all("h3"):
    a = i.find("a")
    title = a.get("title")
    names.append(title)

prices= soup.find_all("p",{"class": "price_color"})

for name,price in zip(names,prices):
    print("İsim : ",name)
    print("Fiyat : ",price.text)