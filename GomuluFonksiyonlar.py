from functools import reduce
# Map fonksiyonu ile tuple içindeki kenarların alanlarını hesaplama

kenarlar_listesi=[(3,4),(10,3),(5,6),(1,9)]
def carpim (x,y):
    return x*y

print(list(map(lambda x: carpim(x[0], x[1]), kenarlar_listesi)))

# Filter fonksiyonu ile üçgen olup olmadığını kontrol etme

ucgenİhtimal_listesi=[(3,4,5),(6,8,10),(3,10,7)]

def ucgenmi(t):
    x, y, z = t
    return abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z

print(list(filter(ucgenmi, ucgenİhtimal_listesi)))

# Liste içerisindeki çift sayıları bulup toplamlarını yazdırır. (filter ve reduce ile)

liste=[1,2,3,4,5,6,7,8,9,10]

def ciftmi(sayi):
    
    if(sayi%2==0):
        return sayi

ciftlerlistesi=list(filter(ciftmi,liste))

def toplam(x,y):
    return x+y

print(reduce(toplam,ciftlerlistesi))

# Zip fonksiyonu ile isim soyisim birleştirme

isimler= ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler =["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler, soyisimler):
    print(i,j)