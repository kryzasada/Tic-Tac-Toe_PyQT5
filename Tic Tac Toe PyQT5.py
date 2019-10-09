# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Win(object):
    def setupUi(self, Win):
        Win.setObjectName("Win")
        Win.resize(800, 600)

        self.label_move = []

        self.centralwidget = QtWidgets.QWidget(Win)
        self.centralwidget.setObjectName("centralwidget")


        self.who_move(XY_move)

        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(224, 242, 358, 16))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(224, 342, 358, 16))
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
        font.setPointSize(16)
        self.label_Y.setFont(font)
        self.label_Y.setObjectName("label_Y")

        for x in range(0, 9):
            self.label_move.append(QtWidgets.QLabel(self.centralwidget))


        self.A1 = QtWidgets.QPushButton(self.centralwidget)
        self.A1.setGeometry(QtCore.QRect(250, 190, 71, 41))
        self.A1.setText("")
        self.A1.clicked.connect(lambda: self.move_button("A1", XY_move))

        self.A2 = QtWidgets.QPushButton(self.centralwidget)
        self.A2.setGeometry(QtCore.QRect(370, 190, 71, 41))
        self.A2.setText("")
        self.A2.clicked.connect(lambda: self.move_button("A2", XY_move))

        self.A3 = QtWidgets.QPushButton(self.centralwidget)
        self.A3.setGeometry(QtCore.QRect(493, 190, 71, 41))
        self.A3.setText("")
        self.A3.clicked.connect(lambda: self.move_button("A3", XY_move))



        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(250, 280, 71, 41))
        self.B1.setText("")
        self.B1.clicked.connect(lambda: self.move_button("B1", XY_move))

        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(372, 280, 71, 41))
        self.B2.setText("")
        self.B2.clicked.connect(lambda: self.move_button("B2", XY_move))

        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(493, 280, 71, 41))
        self.B3.setText("")
        self.B3.clicked.connect(lambda: self.move_button("B3", XY_move))



        self.C1 = QtWidgets.QPushButton(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(250, 370, 71, 41))
        self.C1.setText("")
        self.C1.clicked.connect(lambda: self.move_button("C1", XY_move))

        self.C2 = QtWidgets.QPushButton(self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(370, 370, 71, 41))
        self.C2.setText("")
        self.C2.clicked.connect(lambda: self.move_button("C2", XY_move))

        self.C3 = QtWidgets.QPushButton(self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(493, 370, 71, 41))
        self.C3.setText("")
        self.C3.clicked.connect(lambda: self.move_button("C3", XY_move))



        Win.setCentralWidget(self.centralwidget)


        self.retranslateUi(Win)
        QtCore.QMetaObject.connectSlotsByName(Win)

    def retranslateUi(self, Win):
        _translate = QtCore.QCoreApplication.translate
        Win.setWindowTitle(_translate("Win", "Tic-Tac-Toe"))
        self.label_X.setText(_translate("Win", "Player X = " + str(scoreX)))
        self.label_Y.setText(_translate("Win", "Player Y = " + str(scoreY)))


    def move_button(self, position, XY_move):
        print(position)


        if XY_move :
            XY_move = "X"
        else:
            XY_move = "O"


        if position == 'A1':
            self.label_move[0].setGeometry(QtCore.QRect(250, 190, 71, 41))
            self.A1.deleteLater()
            self.A1 = None
            self.label_write(self.label_move[0], XY_move)

        elif position == 'A2':
            self.label_move[1].setGeometry(QtCore.QRect(370, 190, 71, 41))
            self.A2.deleteLater()
            self.A2 = None
            self.label_write(self.label_move[1], XY_move)

        elif position == 'A3':
            self.label_move[2].setGeometry(QtCore.QRect(493, 190, 71, 41))
            self.A3.deleteLater()
            self.A3 = None
            self.label_write(self.label_move[2], XY_move)

        elif position == 'B1':
            self.label_move[3].setGeometry(QtCore.QRect(250, 280, 71, 41))
            self.B1.deleteLater()
            self.B1 = None
            self.label_write(self.label_move[3], XY_move)

        elif position == 'B2':
            self.label_move[4].setGeometry(QtCore.QRect(372, 280, 71, 41))
            self.B2.deleteLater()
            self.B2 = None
            self.label_write(self.label_move[4], XY_move)

        elif position == 'B3':
            self.label_move[5].setGeometry(QtCore.QRect(493, 280, 71, 41))
            self.B3.deleteLater()
            self.B3 = None
            self.label_write(self.label_move[5], XY_move)

        elif position == 'C1':
            self.label_move[6].setGeometry(QtCore.QRect(250, 370, 71, 41))
            self.C1.deleteLater()
            self.C1 = None
            self.label_write(self.label_move[6], XY_move)

        elif position == 'C2':
            self.label_move[7].setGeometry(QtCore.QRect(370, 370, 71, 41))
            self.C2.deleteLater()
            self.C2 = None
            self.label_write(self.label_move[7], XY_move)

        elif position == 'C3':
            self.label_move[8].setGeometry(QtCore.QRect(493, 370, 71, 41))
            self.C3.deleteLater()
            self.C3 = None
            self.label_write(self.label_move[8], XY_move)


    def label_write(self, rr, XY_move):
        rr.setAlignment(QtCore.Qt.AlignCenter)
        rr.setText(QtCore.QCoreApplication.translate("Win", XY_move))

    def who_move(self, XY_move):
        if XY_move:
            self.line_X = QtWidgets.QFrame(self.centralwidget)
            self.line_X.setGeometry(QtCore.QRect(205, 58, 130, 51))
            self.line_X.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_X.setLineWidth(1)
        else:
            self.line_Y = QtWidgets.QFrame(self.centralwidget)
            self.line_Y.setGeometry(QtCore.QRect(475, 58, 130, 51))
            self.line_Y.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_Y.setLineWidth(1)


if __name__ == "__main__":
    scoreX = 0
    scoreY = 0
    XY_move = bool(True)

    app = QtWidgets.QApplication(sys.argv)
    Win = QtWidgets.QMainWindow()
    ui = Ui_Win()
    ui.setupUi(Win)
    Win.show()
    sys.exit(app.exec_())
