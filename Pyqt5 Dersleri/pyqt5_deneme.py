from PyQt5 import QtWidgets
import sys

def pencere ():
    app=QtWidgets.QApplication(sys.argv)
    okay=QtWidgets.QPushButton("Tamam")
    cancel=QtWidgets.QPushButton("İptal")
    

    h_box=QtWidgets.QHBoxLayout()
    

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box=QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt Dersidir")

    pencere.setLayout(v_box)

    pencere.setGeometry(100,100,500,500)
    pencere.show()

    sys.exit(app.exec_())

pencere()