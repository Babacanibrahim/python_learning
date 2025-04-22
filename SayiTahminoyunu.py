import random
import time

print("""
      ***************************
      Sayı tahmin etme oyunu
     **************************
      1 ile 1000 arasında rastgele bir sayıyı bilmeye çalışın.
""")
rnd_nmbr=random.randint(1,1000)
tahmin_hakki=int(input("TAHMİN HAKKINIZI GİRİNİZ : "))
kalan_tahmin=tahmin_hakki


while(tahmin_hakki!=0):
    tahmin=int(input("Bir sayı tahmin edin. : "))

    if(tahmin<rnd_nmbr):
        print("Cevabınız analiz ediliyor...\n")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz..")
        tahmin_hakki-=1
        print("Kalan tahmin hakkınız {}/{}".format(tahmin_hakki,kalan_tahmin))

    elif(tahmin>rnd_nmbr):
        print("Cevabınız analiz ediliyor...\n")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz..")
        tahmin_hakki-=1
        print("Kalan tahmin hakkınız {}/{}".format(tahmin_hakki,kalan_tahmin))


    elif(tahmin==rnd_nmbr):
        print("Tebrikler doğru tahmin ettiniz. {} sayısını doğru bildiniz.!".format(rnd_nmbr))
        break
    else:
        print("Tahmin hakkınız bitti. Sayı {}.".format(rnd_nmbr))
