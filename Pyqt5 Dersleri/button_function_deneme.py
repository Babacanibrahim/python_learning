import sys
from PyQt5 import QtWidgets

class Pencere (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui__init__()

    def ui__init__(self):
        self.yazi_alani=QtWidgets.QLineEdit()
        self.temizle=QtWidgets.QPushButton("Temizle")
        self.yazdır=QtWidgets.QPushButton("Yazdır")
        self.yazi_yeri=QtWidgets.QLabel()

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addWidget(self.yazi_yeri)
        v_box.addStretch()

        self.setLayout(v_box)
        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)

    def click(self):
        sender=self.sender()
        if sender.text()=="Temizle":
            self.yazi_yeri.clear()
        else:
            self.yazi_yeri.setText(self.yazi_alani.text())

app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec_())