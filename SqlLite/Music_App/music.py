import sqlite3
import time

# Şarkıların class ı
class Music():

    def __init__(self,isim,sanatci,album,produksiyon_sirketi,sarki_suresi):
        self.isim=isim
        self.sanatci=sanatci
        self.album=album
        self.produksiyon_sirketi=produksiyon_sirketi
        self.sarki_suresi=sarki_suresi

    def __str__(self):
        return ("Şarkı : {}\nSanatçı : {}\nAlbüm : {}\nProdüksiyon Şirketi : {}\nŞarkı süresi : {}".format(self.isim,self.sanatci,self.album,self.produksiyon_sirketi,self.sarki_suresi))
    
class MusicApp():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_kapat(self):
        self.baglanti.close()

    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("musicapp.db")
        self.cursor=self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Musics (song_name TEXT , singer TEXT , album TEXT , company TEXT , song_time INTEGER)")
        self.baglanti.commit()

# Şarkıları listeleyen metod
    def get_all_musics(self):
        self.cursor.execute("SELECT song_name FROM Musics")
        muzikler=self.cursor.fetchall()
        
        if(len(muzikler)==0):
            print("Hiç şarkı bulunmuyor.")
        else:
            for i in muzikler:
                muzik=i[0]  
                print(muzik)

# Şarkı ekleyen metod
    def add_songs(self,music):
        self.cursor.execute("INSERT INTO Musics values (?,?,?,?,?)",(music.isim,music.sanatci,music.album,music.produksiyon_sirketi,music.sarki_suresi))
        self.baglanti.commit()

# Şarkı silen metod
    def delete_music(self,isim):
        self.cursor.execute("DELETE FROM Musics where song_name=(?)",(isim,))
        self.baglanti.commit()

# Şarkının sanatçısını güncelleyen metod
    def update_singer(self,music,yeni_sanatci):
        self.cursor.execute("UPDATE Musics set singer=(?) where song_name=(?)",(yeni_sanatci,music))
        self.baglanti.commit()

# Toplam şarkı süresini bulma
    def total_song_time(self):
        self.cursor.execute("SELECT SUM(song_time) FROM Musics")
        toplam_saniye = self.cursor.fetchone()[0]
    
        if toplam_saniye is None:
            print("Henüz şarkı eklenmemiş.")
        else:
            dakika = toplam_saniye // 60
            saniye = toplam_saniye % 60
            print("Toplam şarkı süresi: {} dakika {} saniye".format(dakika,saniye))

# Sanatçıları listeleyen metod
    def get_singers(self):
        self.cursor.execute("SELECT DISTINCT singer from Musics")
        singers=self.cursor.fetchall()
        for i in singers:
            sanatci=i[0]
            print(sanatci)
