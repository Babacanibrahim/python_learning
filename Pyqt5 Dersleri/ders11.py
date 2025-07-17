import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu (QMainWindow):
    def __init__(self):
        super().__init__()
        menubar=self.menuBar()
        