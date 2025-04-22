class Computer() :
    def __init__(self,marka,fiyat,işlemci,stok_adedi=0):
        self.marka=marka
        self.fiyat=fiyat
        self.işlemci=işlemci
        self.stok_adedi=stok_adedi

    def __str__(self):
        print("Bilgisayar bilgileri \n Marka : {}\n Fiyat : {}\n İşlemci : {}\n Stok adedi : {} ".format(self.marka,self.fiyat,self.işlemci,self.stok_adedi))

    def __len__(self):
        print(self.stok_adedi)

computer=Computer("Asus",45000,"i5",15)
computer.__str__()
computer.__len__()
computer.marka="Monster"

computer.__str__()