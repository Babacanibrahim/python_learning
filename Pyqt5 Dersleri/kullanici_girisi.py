import sys
from PyQt5 import QtWidgets
import sqlite3

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
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.button=QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.button)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.button.clicked.connect(self.click)

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



app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec_())