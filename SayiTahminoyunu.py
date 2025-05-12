import random
import time

print("""
      ***************************
      Sayı tahmin etme oyunu
     **************************
      1 ile 1000 arasında rastgele bir sayıyı bilmeye çalışın.
""")
rnd_nmbr = random.randint(1, 1000)
tahmin_hakki = int(input("TAHMİN HAKKINIZI GİRİNİZ : "))
kalan_tahmin = tahmin_hakki

while tahmin_hakki > 0:
    tahmin = int(input("Bir sayı tahmin edin: "))

    print("Cevabınız analiz ediliyor...\n")
    time.sleep(1)

    if tahmin == rnd_nmbr:
        print(f"Tebrikler doğru tahmin ettiniz. {rnd_nmbr} sayısını doğru bildiniz!")
        break
    else:
        tahmin_hakki -= 1
        if tahmin_hakki == 0:
            print(f"Tahmin hakkınız bitti. Sayı {rnd_nmbr}.")
            break
        elif tahmin < rnd_nmbr:
            print("Daha büyük bir sayı giriniz..")
        else:
            print("Daha küçük bir sayı giriniz..")
        print("Kalan tahmin hakkınız {}/{}".format(tahmin_hakki, kalan_tahmin))