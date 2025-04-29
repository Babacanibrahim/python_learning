from supermarket import *
import time
from wallet import*
from Product import*

print("""
**************************************************
      
    MAĞAZAMIZA HOŞ GELDİNİZ
      
**************************************************

      1- Bakiye görüntüle
      2- Hesaba para yükle
      3- Ürünleri listele
      4- Ürün ekle
      5- Ürün sil
      6- Ürün satın al
      7- Ürün güncelle
      8- Çıkış

      """)

sprmrkt=SuperMarket()
wallet=Wallet()

while(True):
    secim=input("\nLütfen işleminizi seçiniz : ")

    if (secim=="1"):
        wallet.check_balance()

    elif(secim=="2"):
        para=int(input("\nYüklemek istediğiniz miktarı girin : "))
        wallet.deposit(para)
    
    elif(secim=="3"):
        sprmrkt.list_products()

    elif(secim=="4"):
        name=input("Ürün adı : ")
        category=input("Ürün kategorisi : ")
        price= int(input("Ürün fiyatı : "))
        stock_amount=int(input("Ürün adedi : "))

        product=Product(name,category,price,stock_amount)

        sprmrkt.add_product(product)

    elif(secim=="5"):
        name=input("Silmek istediğiniz ürünün adını giriniz : ")
        sprmrkt.delete_product(name)
        print(name," ürünü silindi.")

    elif (secim=="6"):
        sprmrkt.list_products_buy()
        name=input("\nSatın almak istediğiniz ürünün adını giriniz : ")
        # ürünün fiyatına erişmeyle devam edicem
        