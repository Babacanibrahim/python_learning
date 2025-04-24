# MÜKEMMEL SAYIALRI BULMA (ARALIK 1-1000)
def mukemmelSayi(sayi):
    total=0
    for i in range (1,sayi):
        if sayi%i==0:
            total=total+i
    if total==sayi:
        return True
    else:
        return False

for i in range (1,1001):
    if mukemmelSayi(i)==True:
        print(i) 

# EBOBLARI BULUP DÖNDÜREN METHOD

def EBOB(a,b):
    liste_a=[]
    liste_b=[]
    for i in range (1,a+1):
        if a%i==0:
            liste_a.append(i)
    
    for j in liste_a:
        if b%j==0:
            liste_b.append(j)

    return max(liste_b)
print(EBOB(150,60)) 

# İKİ BASAMAKLI SAYI OKUNUŞU

birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10
    
    return onlar[ikinci] + " " + birler[birinci]

    
sayı =  int(input("Sayı:"))
print(okunus(sayı)) 

# EKOK BULAN PROGRAM

def EKOK(a,b):
    i=1
    while(True):
        if(i%a==0 and i%b==0):
            return i
        else:
            i=i+1     
        
print(EKOK(89,9))

# PİSAGOR ÜÇLÜLERİ BULMA KODU
def pisagorBulma():
    for i in range (1,101):
        for j in range (i,101):
            x=i**2+j**2
            c=x**0.5
        
            if (1<=c<=100 and c.is_integer()):
                print(i,"-",j,"-",int(c))

pisagorBulma()
