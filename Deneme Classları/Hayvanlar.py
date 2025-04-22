class Hayvan():
    def __init__(self,tür,habitat,ses,ayak_sayisi,beslenme_sekli):
        self.habitat=habitat
        self.ses=ses
        self.ayak_sayisi=ayak_sayisi
        self.beslenme_sekli=beslenme_sekli
        self.tür=tür
    
    def __str__(self):
        return f"{self.tür}: {self.ayak_sayisi} ayaklı, Habitat: {self.habitat}, Beslenme: {self.beslenme_sekli}"
    
    def yemekYeme(self):
        print(self.tür+" Yemek yiyiyor.")

    def uyumak(self):
        print(self.tür+" Uyuyor.")

    def sescikarma(self):
        print(self.tür , self.ses ,"diyor.")

class Kedi(Hayvan):
    
    def __init__(self):
        super().__init__("Kedi", "Doğa", "Miyav", 4, "Hepçil")

class At(Hayvan):
    
    def __init__(self):
        super().__init__("At", "Doğa", "İĞHİHĞHİHĞİ", 4, "Otçul")

    def run(self):
        print("At dört nala koşuyor.")

class Kuş(Hayvan):
    
    def __init__(self):
        super().__init__("Kuş", "Hava", "Ck cik", 2, "Otçul")

    def flying(self):
        print("Kuş uçuyor.")


kedi=Kedi()
kedi.sescikarma()
kedi.uyumak()
kedi.yemekYeme()
print(kedi)
print()

kuş=Kuş()
kuş.flying()
kuş.sescikarma()
kuş.uyumak()
kuş.yemekYeme()
print(kuş)
print()

at=At()
at.run()
at.sescikarma()
at.uyumak()
at.yemekYeme()
print(at)