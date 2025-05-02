import requests

doviz_kodlari = {
    "1": "TRY",
    "2": "USD",
    "3": "EUR",
    "4": "NOK",
    "5": "JPY"
}

doviz1=input("""
***************************************
             
        İLK DÖVİZİNİZİ SEÇİN.
             
    1 - TRY
    2 - USD
    3 - EUR
    4 - NOK
    5 - JPY
             
***************************************

      : """)

miktar=float(input("Kaç birim çevirmek istiyorsunuz : "))

doviz2=input("""
***************************************
             
        ÇEVİRMEK İSTEDİĞİNİZ DÖVİZİ SEÇİN.
             
    1 - TRY
    2 - USD
    3 - EUR
    4 - NOK
    5 - JPY
             
***************************************

      : """)

ilk_doviz = doviz_kodlari.get(doviz1)
ikinci_doviz = doviz_kodlari.get(doviz2)

if not ilk_doviz or not ikinci_doviz:
    print(" Geçersiz döviz seçimi yaptınız.")
    exit()

url = "https://data.fixer.io/api/latest?access_key=5c63451843ebbc3b31e66c81e8e9f599"

response = requests.get(url)

data = response.json()

if data.get("success") != True:
    print("Veri alınamadı:")
    exit()

rates = data["rates"]

try:
    miktar_eur = miktar / rates[ilk_doviz]
    cevrilen_miktar = miktar_eur * rates[ikinci_doviz]

    print(f"\n {miktar} {ilk_doviz} ≈ {cevrilen_miktar:.2f} {ikinci_doviz}")
except KeyError:
    print(" Seçilen para birimi bulunamadı.")