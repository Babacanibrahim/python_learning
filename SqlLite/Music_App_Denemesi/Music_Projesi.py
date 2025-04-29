from music import *

print("""
*******************************************
      
    MÜZİK UYGULAMASINA HOŞ GELDİNİZ..!
      
      1- Şarkıları Listele

      2- Şarkı Ekle

      3- Şarkı Sil
      
      4- Şarkı Sanatçısı Güncelle

      5- Sanatçıları Listele

      6- Toplam Şarkı Süresini Görme

      7- Çıkış
      
      
*******************************************
    
      """)
music=MusicApp()

while(True):
    secim=input("Lütfen bir seçim yapınız..! : ")

    if(secim=="1"):
        print("Şarkılar Getiriliyor..!\n*****************")
        time.sleep(1)
        music.get_all_musics()
        print("*****************")
    
    elif(secim=="2"):
        isim=input("Şarkı ismi (vazgeçmek için 'q' basınız.):")
        if isim=="q":
            break
        sarkici=input("Sanatçı ismi :")
        album=input("Şarkının albümü :")
        prod=input("Prodüksiyon şirketi :")
        try:
            timee = int(input("Şarkının süresi (saniye cinsinden) :"))
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
            continue
        print("Yeni şarkı ekleniyor lütfen bekleyiniz...")
        time.sleep(1)
        musicc=Music(isim,sarkici,album,prod,timee)
        music.add_songs(musicc)
        print("Şarkılar başarıyla eklendi...!")

    elif (secim=="3"):
        isim=input("Silmek istediğiniz şarkının adını giriniz :")
        print("ŞARKI ARANIYOR...")
        time.sleep(1)
        music.cursor.execute("SELECT * FROM Musics WHERE song_name=?", (isim,))
        muzik = music.cursor.fetchone()

        if muzik:
            print("ŞARKI SİLİNİYOR...\n")
            time.sleep(1)
            music.delete_music(isim)
            print("ŞARKI SİLİNDİ...\n")
        else:
            print("Böyle bir şarkı bulunamadı.")

    elif (secim=="4"):
        isim=input("Sanatçısını güncellemek istediğiniz şarkının adını giriniz :")
        print("ŞARKI ARANIYOR...")
        time.sleep(1)
        music.cursor.execute("SELECT * FROM Musics WHERE song_name=?", (isim,))
        muzik = music.cursor.fetchone()

        if muzik:
            sanatci=input("Yeni sanatçının ismini giriniz : ")
            print("ŞARKI VE SANATÇISI GÜNCELLENİYOR...\n")
            time.sleep(1)
            music.update_singer(isim,sanatci)
            print("ŞARKI VE SANATÇISI GÜNCELLENDİ ")
        else:
            print("Böyle bir şarkı bulunamadı.")

    elif(secim=="5"):
        print("SANATÇILAR GETİRLİYOR\n*****************")
        time.sleep(1)
        music.get_singers()
        print("*****************")

    elif (secim=="6"):
        print("TOPLAM ŞARKI SÜRESİ HESAPLANIYOR...")
        time.sleep(1)
        music.total_song_time()
    
    elif secim=="7":
        print("UYGULAMADAN ÇIKIŞ YAPILIYOR...")
        time.sleep(1)
        music.baglanti_kapat()
        print("YİNE BEKLERİZ...")
        break
    else:
        print("Geçersiz bir seçim yaptınız..!")