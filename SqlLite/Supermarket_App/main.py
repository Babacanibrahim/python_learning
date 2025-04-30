from supermarket import SuperMarket
import time
from wallet import Wallet
from product import Product

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
        print("Bakiyeniz hesaplanıyor...")
        time.sleep(1)
        wallet.check_balance()

    elif(secim=="2"):
        try:
            para=int(input("\nYüklemek istediğiniz miktarı girin : "))
            print("Bakiyeniz güncelleniyor...")
            time.sleep(1)
            wallet.deposit(para)
        except:
            print("***  Lütfen tamsayı cinsinden bir değer girin. ***\n")
    
    elif(secim=="3"):
        print("Lütfen bekleyiniz...")
        print("")
        time.sleep(1)
        sprmrkt.list_products()

    elif(secim=="4"):
        name=input("Ürün adı : ")
        category=input("Ürün kategorisi : ")
        price= int(input("Ürün fiyatı : "))
        stock_amount=int(input("Ürün adedi : "))

        product=Product(name,category,price,stock_amount)
        time.sleep(1)
        sprmrkt.add_product(product)

    elif(secim=="5"):
        name=input("Silmek istediğiniz ürünün adını giriniz : ")
        time.sleep(1)
        sprmrkt.delete_product(name)

    elif (secim == "6"):
        sprmrkt.list_products_buy()
        name = input("\nSatın almak istediğiniz ürünün adını giriniz : ")
        price = sprmrkt.price_product(name)
        time.sleep(1)

        if price is None:
            print("Ürün bulunamadı veya fiyat hatalı.")
        elif wallet.balance >= price:
            sprmrkt.buy_product(name)
            wallet.buy_product(price)

        else:
            print("Yetersiz bakiye.")

    elif (secim=="7"):
        name=input("Güncellemek istediğiniz ürünün adı : ")
        time.sleep(1)
        if sprmrkt.product_exists(name):
            product_name=input("Yeni ürün adı : ")
            category=input("Yeni ürün kategorisi : ")
            price= int(input("Yeni ürün fiyatı : "))
            stock_amount=int(input("Yeni ürün adedi : "))
            product=Product(product_name,category,price,stock_amount)
            time.sleep(1)
            sprmrkt.update_product(name,product)
        else:
            print("Ürün bulunamadı.")

    elif (secim=="8"):
        print("ÇIKIŞ YAPILIYOR...")
        time.sleep(1)
        sprmrkt.baglanti_kapat()
        print("YİNE BEKLERİZ.!")
    
    else:
        print("GEÇERSİZ SEÇİM YAPTINIZ TEKRAR DENEYİN.!")

        