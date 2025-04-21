# Kolay alıştırmalar

a = int(input("1. sayıyı giriniz: "))
b = int(input("2. sayıyı giriniz: "))
c = int(input("3. sayıyı giriniz: "))

sonuc = a*b*c

print("Girdiğiniz sayılar {} , {} , {}  sonucunuz : {} ".format(a,b,c,sonuc))

# Vücut kitle indeks hesaplama

boy = float(input("Boyunuzu cm cinsinden giriniz : "))
kilo = float(input("Kilonuzu kg cinsinden giriniz : "))

gercekboy=boy/100*boy/100
VKİ=kilo/gercekboy
print(VKİ)

# Kolay alıştırmalar 2

ad=input("ADINIZ : ")
soyad=input("SOYADINIZ : ")
no=input("NUMARANIZ : ")

bilgiler=[ad,soyad,no]

print("Kullanıcı bilgileri :\nAD : {}\nSoyad : {}\nNumarası : {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

# Hipotenüs bulma

a=int(input("1. dik kenarı girin : "))
b=int(input("2. dik kenarı girin : "))

hipotenus=((a*a)+(b*b))**0.5

print(hipotenus)