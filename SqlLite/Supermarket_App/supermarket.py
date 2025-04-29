import sqlite3

class SuperMarket():

#init function
    def __init__(self):
        self.baglanti_olustur()

# Connection close
    def baglanti_kapat(self):
        self.baglanti.close()

# Create database and table
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("supermarket.db")
        self.cursor=self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Products (name TEXT , category TEXT , price INT , stock_amount INT)")
        self.baglanti.commit()

# Listing products
    def list_products(self):
        self.cursor.execute("SELECT * FROM Products")
        products=self.cursor.fetchall()

        for i in products:
            product=(i[0],i[1],i[2],i[3])
            print(product,"\n***************************************")

# Add product
    def add_product(self,product):
        self.cursor.execute("INSERT INTO Products values (?,?,?,?)",(product.name,product.category,product.price,product.stock_amount))
        self.baglanti.commit()
        print(product.name," başarıyla eklendi.")

# Find the product
    def product_exists(self, name):
        self.cursor.execute("SELECT 1 FROM Products WHERE name = ?", (name,))
        return self.cursor.fetchone() is not None


# Delete product
    def delete_product(self,name):
        if self.product_exists(name):
            self.cursor.execute("DELETE FROM Products WHERE name=?",(name,))
            self.baglanti.commit()
        else:
            print("Ürün bulunamadı.")

# Buy product
    def buy_product(self,name):
        self.cursor.execute("SELECT stock_amount FROM Products where name =?",(name,))
        result=self.cursor.fetchone()

        if result is None:
            print("Ürün bulunamadı.")
            return
        stock_amount=result[0]

        if stock_amount>0:
            stock_amount-=1
            self.cursor.execute("UPDATE Products SET stock_amount=? WHERE name =?",(stock_amount,name))
            self.baglanti.commit()
            print(name ," ürününüz başarıyla satın alındı.")
        else:
            print("Seçtiğiniz ürünün stoğu maalesef tükendi.")

# Update product
    def update_product(self,name,product):
        if self.product_exists(name):
            self.cursor.execute("UPDATE Products SET name=? , category=? , price=? , stock_amount=? WHERE name=?",(product.name,product.category,product.price,product.stock_amount,name))
            self.baglanti.commit()
            print("Ürün başarıyla güncellendi.")
        else:
            print("Ürün bulunamadı")

# Listing products for buy
    def list_products_buy(self):
        self.cursor.execute("SELECT name FROM Products")
        products=self.cursor.fetchall()

        for i in products:
            print(i[0])