# ASAL MI KODU

def asalMi(sayi):
    if(sayi==2):
        print(sayi , "asaldır.")
    elif (sayi>2):
        sayac=0
        for i in range(2,sayi):
            if sayi%i==0:
                sayac+=1
        if(sayac==0):
            print(sayi , "asaldır.")

        else:
            print(sayi , "asal değildir.")

    else:
        print(sayi , "asal değildir.")
        

# TAM BÖLENLERİ BULMA

liste=[]
def tamBolenBulma(sayi):
    for i in range (1,sayi+1):
        if(sayi%i==0):
            liste.append(i)
    print(liste)

tamBolenBulma(850)
asalMi(3)