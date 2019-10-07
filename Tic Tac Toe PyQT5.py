# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Win(object):
    def setupUi(self, Win):
        Win.setObjectName("Win")
        Win.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(Win)
        self.centralwidget.setObjectName("centralwidget")

        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(224, 242, 351, 16))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(224, 342, 351, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(330, 170, 16, 261))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(470, 170, 16, 261))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.label_X = QtWidgets.QLabel(self.centralwidget)
        self.label_X.setGeometry(QtCore.QRect(210, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_X.setFont(font)
        self.label_X.setObjectName("label_X")

        self.label_Y = QtWidgets.QLabel(self.centralwidget)
        self.label_Y.setGeometry(QtCore.QRect(480, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Y.setFont(font)
        self.label_Y.setObjectName("label_Y")

        self.label_A1 = QtWidgets.QLabel(self.centralwidget)
        self.label_A1.setGeometry(QtCore.QRect(250, 190, 71, 41))
        self.label_A1.setAlignment(QtCore.Qt.AlignCenter)


        self.A1 = QtWidgets.QPushButton(self.centralwidget)
        self.A1.setGeometry(QtCore.QRect(250, 190, 71, 41))
        self.A1.setText("")
        self.A1.setObjectName("A1")
        self.A1.clicked.connect(self.move)

        self.A2 = QtWidgets.QPushButton(self.centralwidget)
        self.A2.setGeometry(QtCore.QRect(370, 190, 71, 41))
        self.A2.setText("")
        self.A2.setObjectName("A2")

        self.A3 = QtWidgets.QPushButton(self.centralwidget)
        self.A3.setGeometry(QtCore.QRect(490, 190, 71, 41))
        self.A3.setText("")
        self.A3.setObjectName("A3")



        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(250, 280, 71, 41))
        self.B1.setText("")
        self.B1.setObjectName("B1")

        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(370, 280, 71, 41))
        self.B2.setText("")
        self.B2.setObjectName("B2")

        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(490, 280, 71, 41))
        self.B3.setText("")
        self.B3.setObjectName("B3")



        self.C1 = QtWidgets.QPushButton(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(250, 370, 71, 41))
        self.C1.setText("")
        self.C1.setObjectName("C1")

        self.C2 = QtWidgets.QPushButton(self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(370, 370, 71, 41))
        self.C2.setText("")
        self.C2.setObjectName("C2")

        self.C3 = QtWidgets.QPushButton(self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(490, 370, 71, 41))
        self.C3.setText("")
        self.C3.setObjectName("C3")


        Win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Win)
        QtCore.QMetaObject.connectSlotsByName(Win)

    def retranslateUi(self, Win):
        _translate = QtCore.QCoreApplication.translate
        Win.setWindowTitle(_translate("Win", "Tic-Tac-Toe"))
        self.label_X.setText(_translate("Win", "Player X = "))
        self.label_Y.setText(_translate("Win", "Player Y = "))



    def move(self):
        _translate = QtCore.QCoreApplication.translate
        print("działa move")
        self.A1.deleteLater()
        self.A1 = None
        self.label_A1.setText(_translate("Win", "X"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Win = QtWidgets.QMainWindow()
    ui = Ui_Win()
    ui.setupUi(Win)
    Win.show()
    sys.exit(app.exec_())
