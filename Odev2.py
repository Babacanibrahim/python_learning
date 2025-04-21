# Vücut kitle indeksine göre bilgi yazdırma

boy=float(input("Boyunuzu girin: "))
kilo=float(input("Kilonuzu girin: "))

BKİ =kilo/boy*boy

if (BKİ<18.5) :
    print("Zayıf")
elif(18.5<BKİ<25):
    print("Normal")
elif(25<BKİ<30):
    print("Obez")
else:
    print("Aşırı obez")

# Girilen sayılardan en büyüğünü bulma

a=int(input("1. sayı :"))
b=int(input("2. sayı :"))
c=int(input("3. sayı :"))

if(a>b and a>c):
    print("En büyük sayı",a)
elif(b>a and b>c):
    print("En büyük sayı",b)
if(c>a and c>b):
    print("En büyük sayı",c)

# Notlara göre harf notu belirleme

vize1=float(input("1. vize: "))
vize2=float(input("2. vize: "))
final=float(input("Final : "))

ort = (vize1*3/10)+(vize2*3/10)+(final*4/10)
print(ort)
if(ort>=90):
    print("AA")
elif(ort>=85):
    print("BA")
elif(ort>=80):
    print("BB")
elif(ort>=75):
    print("CB")
elif(ort>=65):
    print("CC")
elif(ort>=60):
    print("DC")
else:
    print("KALDIN MAALESEF")

# Üçgen veya dörtgenin tipini belirleme

cokgen=int(input("""
    *************************************        
        Dörtgen veya üçgen seçimi yapın.
             
    1- Üçgen
             
    2- Dörtgen
             
    *************************************        
    
"""))

# Üçgense

if(cokgen==1):
    print("3 tane kenar giriniz : ")
    a=int(input("1. kenar giriniz : "))
    b=int(input("2. kenar giriniz : "))
    c=int(input("3. kenar giriniz : "))

    if(a==b==c):
        print("Eşkenar bir üçgen seçtiniz.")
    elif((a*a)+(b*b)==(c*c) or (c*c)+(b*b)==(a*a) or (a*a)+(c*c)==(b*b)  ) :
        print("Dik üçgen seçmişsiniz.")
    elif(abs(c-b)<a<c+b or abs(a-b)<c<a+b or abs(a-c)<b<a+c):
        print("Normal bir üçgen seçmişsiniz.")
    elif(a==b!=c or a==c!=b or b==c!=a):
        print("İkizkenar üçgen girmişsiniz.")
    else :
        print("Verdiğiniz kenarlar bir üçgen belirtmiyor.")

#   Eğer dörtgense 

elif(cokgen==2):
    print("4 tane kenar giriniz.")
    k=int(input("1. kenar giriniz : "))
    l=int(input("2. kenar giriniz : "))
    m=int(input("3. kenar giriniz : "))
    n=int(input("4. kenar giriniz : "))

    if (k==l==m==n):
        print("Kare seçmişsiniz.")
    elif(k==l and m==n and k!=m or k==m and l==n and k!=l or k==n and m==l and k!=m or 
         l==m and k==n and l!=k or l==n and m==k and l!=m or m==n and k==l and l!=m):
        print("Dikdörtgen seçmişsiniz.")
    else :
        print("Normal bir dörtgen girmişsiniz.")
else :
    print("Hatalı bir seçim yaptınız...!")