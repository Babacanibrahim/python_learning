from kütüphane import *

print("""
***********************************
      
KÜTÜPHANE PROGRAMINA HOŞGELDİNİZ
      
***********************************
    1- Kitapları listele
    
    2- Kitap ekle
      
    3- Kitap sil
      
    4- Kitap yazarını güncelle
      
    5- Sistemden çıkış

      """)

kutuphane=Kütüphane()
while(True):
    secim=input(" SEÇİMİNİZİ GİRİNİZ : ")

    if (secim=="1"):
        print("KİTAP BİLGİLERİ GETİRİLİYOR...\n")
        time.sleep(1)
        kutuphane.get_all_books()
    
    elif secim=="2":
        isim=input("Kitap ismi :")
        yazar=input("Yazar ismi :")
        yayinevi=input("Yayınevi :")
        tur=input("Kitap türü :")
        kitap=Kitap(isim,yazar,yayinevi,tur)
        print("KİTAP EKLENİYOR...\n")
        time.sleep(1)
        kutuphane.add_book(kitap)
        print("KİTAP EKLENDİ...")

    elif secim=="3":
        isim = input("Silmek istediğiniz kitabın ismini giriniz: ")
        print("KİTAP ARANIYOR...")
        time.sleep(1)
        kutuphane.cursor.execute("SELECT * FROM kitaplar WHERE İsim=?", (isim,))
        kitap = kutuphane.cursor.fetchone()

        if kitap:
            print("KİTAP SİLİNİYOR...\n")
            time.sleep(1)
            kutuphane.delete_book(isim)
            print("KİTAP SİLİNDİ...\n")
        else:
            print("Böyle bir kitap bulunamadı.")


    elif secim=="4":
        isim=input("Yazarını güncellemek istediğiniz kitabın ismini giriniz : ")
        yazar=input("Yeni yazarın adını giriniz : ")
        print("YAZAR GÜNCELLENİYOR...\n")
        kutuphane.update_author(isim,yazar)
        print("YAZAR GÜNCELLENDİ...")

    elif secim=="5":
        print("SİSTEMDEN ÇIKILIYOR...")
        time.sleep(1)
        kutuphane.baglanti.close()
        print("YİNE BEKLERİZ...")
        break
    else:
        print("HATALI SEÇİM YAPTINIZ KONTROL EDİNİZ...")