# Mükemmel sayı bulma

mukemmelSayi=int(input("Bir sayı giriniz : "))

total =0

for i in range(1,(mukemmelSayi)):
    if(mukemmelSayi%i==0):
        total=total+i

if(total==mukemmelSayi):
    print("Sayınız mükemmel sayıdır.")
else:
    print("Sayı mükemmel değildir.")

# Armstrong sayı bulma

sayi=input("Bir sayı giriniz : ")

basamaksayisi=len(sayi)

intsayi=int(sayi)
liste=list()
total=0
for i in sayi:
    degisken=int(i)
    liste.append(degisken)

for i in liste:
    total=total+(i**basamaksayisi)

if total==intsayi:
    print("Sayınız armstrongtur.")
else:
    print("Sayı armstrong değil.")

# Kolay alıştırmalar
for i in range(1,11):
    for j in range (1,11):
        print("{} x {} = {}".format(i,j,(i*j)))
    print()


for i in range (1,101):
    if(i%3==0):
        print(i)

# Girilen sayıları sistemden çıkış yapılana kadar toplayan araç

print("""

***********************************************
      
      SAYI TOPLAMA ARACI

***********************************************
      
      """)

toplam=0
while(True):
    
    sayi=input("Bir sayı giriniz : ")

    if(sayi=="q"):
        print("Uygulamadan çıkılıyor. Sayılarınızın toplamı : {}".format(toplam))
        break
    try:
        intsayi=int(sayi)
        toplam=toplam+intsayi
    except:
        if(sayi!="q"):
            print("Bir tam sayı girmediniz.")

# List comprehension denemesi

liste=[i for i in range (1,51)]

liste2=[i*2 for i in liste]
print(liste2)