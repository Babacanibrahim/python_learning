import sqlite3

con=sqlite3.connect("kütüphane.db")
cursor=con.cursor()

# Tablo oluşturan metod
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT, Yazar TEXT , Yayınevi TEXT , sayfa_sayisi INT)")
    con.commit()

# create_table()

# Veri ekleyen metod
def add_Data(isim,yazar,yayınevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayisi))
    con.commit()

# Verilerin hepsini getiren metod
def get_all():
    cursor.execute("Select * from kitaplık")
    liste=cursor.fetchall()
    for i in liste:
        print(i)

# Verileri isme göre getiren metod
def get_by_isim(isim):
    cursor.execute("Select * from kitaplık where İsim=(?)",(isim,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)

# Paramtereye göre sayfa sayısı güncelleyen metod
def update_by_sayfa_sayisi(yenisayfa,eskisayfa):
    cursor.execute("Update kitaplık set sayfa_sayisi =(?) where sayfa_sayisi =(?)",(yenisayfa,eskisayfa))
    con.commit()

# Kitap adına göre verileri silen metod
def delete_data(isim):
    cursor.execute("Delete from kitaplık where İsim=(?)",(isim,))
    con.commit()


con.close()