# Listedeki elemanları integer değere döndürmeye çalışan metod
def convertToInteger(list):
    result = []  # Sonuç listesi
    for i in list:
        try:
            a = int(i)
            result.append(a)  # Başarıyla dönüştürülünce ekliyoruz
        except ValueError:
            continue
    return result  # Sonuç listesi döndürülüyor

# Listedeki çift sayılar bulup döndüren ve eğer sıradaki sayı tek sayıysa exception fırlatan metod
def findEvenNumber(sayi):
    if(sayi % 2 != 0):
        raise ValueError(f"{sayi} çift sayı değildir.")
    else:
        return sayi

# Listeyi gezip, çift sayıları bulalım ve ortalama hesaplayalım
liste4 = [5, 9, 11, 65, 33, 45, 97, 19, 57]
liste3 = []

for i in liste4:
    try:
        liste3.append(findEvenNumber(i))  # Çift sayıları ekliyoruz
    except ValueError:
        continue

# Ortalama hesaplama kısmı
if liste3:
    toplam = sum(liste3)
    ort = toplam / len(liste3)
    print(ort)
else:
    print("Liste boş olduğundan ortalama hesaplanamaz.")