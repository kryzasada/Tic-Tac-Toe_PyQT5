from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(800,500,300,100)
    win.setWindowTitle("Tic Tac Toe")

    win.show()
    sys.exit(app.exec())

window()
