import sqlite3
import time

# Kitap classı
class Kitap():
    def __init__(self,isim,yazar,yayinevi,tur):
        self.isim=isim
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.tur=tur
    
    def __str__(self):
        return ("Kitap adı : {}\nYazar adı : {}\nYayınevi : {}\nKitap türü : {}".format(self.isim,self.yazar,self.yayinevi,self.tur))

# Kütüphane classı
class Kütüphane():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_kapat(self):
        self.baglanti.close()

# Database oluşturma
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("kütüphane.db")
        self.cursor=self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar(İsim TEXT, Yazar TEXT , Yayınevi TEXT , Tür TEXT)")
        self.baglanti.commit()

# Tüm kitapları getiren metod
    def get_all_books(self):
        self.cursor.execute("Select * from kitaplar")
        kitaplar=self.cursor.fetchall()

        if(len(kitaplar)==0):
            print("Hiç kitap bulunmuyor.")
        else:
            for i in kitaplar:
                kitap=Kitap(i[0],i[1],i[2],i[3])
                print(kitap)
                print("****************")

# Kitap ekleme metodu
    def add_book(self,kitap):
        self.cursor.execute("Insert into kitaplar Values(?,?,?,?)",(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur))
        self.baglanti.commit()

# Kitap silme metodu
    def delete_book(self,isim):   
        self.cursor.execute("Delete from kitaplar where İsim=(?)",(isim,))
        self.baglanti.commit()

# Kitap yazarını güncelleyen metod
    def update_author(self,isim,yeni_yazar):
        self.cursor.execute("Update kitaplar set Yazar =(?) where İsim=(?)",(yeni_yazar,isim))
        self.baglanti.commit()