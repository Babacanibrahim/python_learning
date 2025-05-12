import sys
from PyQt5 import QtWidgets

class Pencere (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani=QtWidgets.QLabel("Henüz tıklanmadı...")
        self.buton=QtWidgets.QPushButton("Bana tıkla.")
        self.say=0

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.buton.clicked.connect(self.click)
    def click(self):
        self.say+=1
        self.yazi_alani.setText("Bana {} kez tıklandı".format(self.say))


app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec_())