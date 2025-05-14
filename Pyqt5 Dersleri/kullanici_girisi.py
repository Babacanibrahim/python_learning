import sys
from PyQt5 import QtWidgets
import sqlite3
from PyQt5.QtCore import QTimer

class Pencere (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglanti_olustur()

    def baglanti_olustur(self):
        baglanti=sqlite3.connect("database.db")
        self.cursor=baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler (kullanici_adi TEXT , parola TEXT)")
        baglanti.commit()

    def init_ui(self):
        self.kullanici_adi=QtWidgets.QLineEdit()
        self.kullanici_adi.setPlaceholderText("Kullanıcı Adı")
        self.parola=QtWidgets.QLineEdit()
        self.parola.setPlaceholderText("Parola")
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.button=QtWidgets.QPushButton("Giriş Yap")
        self.buttonRegister=QtWidgets.QPushButton("Üyelik oluştur")
        self.yazi_alani=QtWidgets.QLabel("")

        self.setWindowTitle("Giriş Ekranı")
        self.resize(300, 150)
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.button)
        v_box.addWidget(self.buttonRegister)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.button.clicked.connect(self.click)
        self.buttonRegister.clicked.connect(self.register)

    def register(self):
        register.show()
        pencere.hide()

    def click(self):
        kullanici_adi=self.kullanici_adi.text()
        parola=self.parola.text()

        try:
            self.cursor.execute("SELECT parola from uyeler WHERE kullanici_adi=?",(kullanici_adi,))
            kayit=self.cursor.fetchone()

            if kayit is None:
                self.yazi_alani.setText("Kullanıcı bulunamadı.")
            elif kayit[0]==parola:
                self.yazi_alani.setText("Giriş başarılı. Hoşgeldin {}".format(self.kullanici_adi.text()))
            else:
                self.yazi_alani.setText("Şifreniz yanlış. {}".format(self.kullanici_adi.text()))
        except Exception as e:
            self.yazi_alani.setText(f"Bir hata oluştu: {str(e)}")

class Register (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.init_ui()

    def init_ui(self):
        self.kullanici_adi=QtWidgets.QLineEdit()
        self.kullanici_adi.setPlaceholderText("Kullanıcı Adı")
        self.parola=QtWidgets.QLineEdit()
        self.parola.setPlaceholderText("Parola")
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.button=QtWidgets.QPushButton("Kayıt Ol")
        self.buttonCancel=QtWidgets.QPushButton("İptal")
        self.yazi_alani=QtWidgets.QLabel("")

        self.setWindowTitle("Kayıt Ekranı")
        self.resize(300, 150)

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.button)
        v_box.addWidget(self.buttonCancel)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.button.clicked.connect(self.click)
        self.buttonCancel.clicked.connect(self.cancel)

    def cancel(self):
        register.hide()
        pencere.show()

    def redirect(self):
        self.hide()
        pencere.show()

    def click (self):
        kullanici_adi=self.kullanici_adi.text()
        parola=self.parola.text()

        try:
            self.cursor.execute("SELECT kullanici_adi from uyeler WHERE kullanici_adi=?",(kullanici_adi,))

            kayit=self.cursor.fetchone()

            if kayit is None:
                self.cursor.execute("INSERT INTO uyeler (kullanici_adi, parola) VALUES (?, ?)", (kullanici_adi, parola))
                self.conn.commit()
                self.yazi_alani.setText("KAYIT BAŞARILI YÖNLENDİRİLİYORSUNUZ..")
                QTimer.singleShot(1000, self.redirect)

            else:
                self.yazi_alani.setText("Bu kullanıcı adı daha önce alınmış.")
        except Exception as e:
            self.yazi_alani.setText(f"Bir hata oluştu: {str(e)}")



app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
register=Register()
pencere.show()
sys.exit(app.exec_())