# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_mainWindow(object):


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)



        self.labelBehindButton = []

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.who_move(whoMove)

        self.horizontalTop = QtWidgets.QFrame(self.centralwidget)
        self.horizontalTop.setGeometry(QtCore.QRect(224, 242, 358, 16))
        self.horizontalTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalTop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalTop.setObjectName("horizontalTop")

        self.horizontalBottom = QtWidgets.QFrame(self.centralwidget)
        self.horizontalBottom.setGeometry(QtCore.QRect(224, 342, 358, 16))
        self.horizontalBottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalBottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalBottom.setObjectName("horizontalBottom")

        self.uprightLeft = QtWidgets.QFrame(self.centralwidget)
        self.uprightLeft.setGeometry(QtCore.QRect(330, 170, 16, 261))
        self.uprightLeft.setFrameShape(QtWidgets.QFrame.VLine)
        self.uprightLeft.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uprightLeft.setObjectName("uprightLeft")

        self.uprightRight = QtWidgets.QFrame(self.centralwidget)
        self.uprightRight.setGeometry(QtCore.QRect(470, 170, 16, 261))
        self.uprightRight.setFrameShape(QtWidgets.QFrame.VLine)
        self.uprightRight.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uprightRight.setObjectName("uprightRight")


        self.labelPlayerX = QtWidgets.QLabel(self.centralwidget)
        self.labelPlayerX.setGeometry(QtCore.QRect(210, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelPlayerX.setFont(font)
        self.labelPlayerX.setObjectName("labelPlayerX")

        self.labelPlayerY = QtWidgets.QLabel(self.centralwidget)
        self.labelPlayerY.setGeometry(QtCore.QRect(480, 40, 131, 51))
        font.setPointSize(16)
        self.labelPlayerY.setFont(font)
        self.labelPlayerY.setObjectName("labelPlayerY")

        for x in range(0, 9):
            self.labelBehindButton.append(QtWidgets.QLabel(self.centralwidget))


        self.buttonTopLeft = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTopLeft.setGeometry(QtCore.QRect(250, 190, 71, 41))
        self.buttonTopLeft.setText("")
        self.buttonTopLeft.clicked.connect(lambda: self.del_button("A1"))

        self.buttonTopMid = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTopMid.setGeometry(QtCore.QRect(370, 190, 71, 41))
        self.buttonTopMid.setText("")
        self.buttonTopMid.clicked.connect(lambda: self.del_button("A2"))

        self.uttonTopRight = QtWidgets.QPushButton(self.centralwidget)
        self.uttonTopRight.setGeometry(QtCore.QRect(493, 190, 71, 41))
        self.uttonTopRight.setText("")
        self.uttonTopRight.clicked.connect(lambda: self.del_button("A3"))



        self.buttonMidLeft = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMidLeft.setGeometry(QtCore.QRect(250, 280, 71, 41))
        self.buttonMidLeft.setText("")
        self.buttonMidLeft.clicked.connect(lambda: self.del_button("B1"))

        self.buttonMidMid = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMidMid.setGeometry(QtCore.QRect(372, 280, 71, 41))
        self.buttonMidMid.setText("")
        self.buttonMidMid.clicked.connect(lambda: self.del_button("B2"))

        self.buttonMidRight = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMidRight.setGeometry(QtCore.QRect(493, 280, 71, 41))
        self.buttonMidRight.setText("")
        self.buttonMidRight.clicked.connect(lambda: self.del_button("B3"))



        self.buttonBottomLeft = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBottomLeft.setGeometry(QtCore.QRect(250, 370, 71, 41))
        self.buttonBottomLeft.setText("")
        self.buttonBottomLeft.clicked.connect(lambda: self.del_button("C1"))

        self.buttonBottomMid = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBottomMid.setGeometry(QtCore.QRect(370, 370, 71, 41))
        self.buttonBottomMid.setText("")
        self.buttonBottomMid.clicked.connect(lambda: self.del_button("C2"))

        self.buttonBottomRight = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBottomRight.setGeometry(QtCore.QRect(493, 370, 71, 41))
        self.buttonBottomRight.setText("")
        self.buttonBottomRight.clicked.connect(lambda: self.del_button("C3"))


        mainWindow.setCentralWidget(self.centralwidget)


        self.retranslate_Ui(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslate_Ui(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Tic-Tac-Toe"))
        self.labelPlayerX.setText(_translate("mainWindow", "Player X = " + str(scoreX)))
        self.labelPlayerY.setText(_translate("mainWindow", "Player Y = " + str(scoreY)))


    def del_button(self, whichButton):
        print(whichButton)

        global whoMove

        if whoMove :
            shapeMove = str('X')
            whoMove = False
        else:
            shapeMove = str("O")
            whoMove = True


        if whichButton == 'A1':
            self.labelBehindButton[0].setGeometry(QtCore.QRect(250, 190, 71, 41))
            self.buttonTopLeft.deleteLater()
            self.buttonTopLeft = None
            self.show_move(self.labelBehindButton[0], shapeMove)

        elif whichButton == 'A2':
            self.labelBehindButton[1].setGeometry(QtCore.QRect(370, 190, 71, 41))
            self.buttonTopMid.deleteLater()
            self.buttonTopMid = None
            self.show_move(self.labelBehindButton[1], shapeMove)

        elif whichButton == 'A3':
            self.labelBehindButton[2].setGeometry(QtCore.QRect(493, 190, 71, 41))
            self.uttonTopRight.deleteLater()
            self.uttonTopRight = None
            self.show_move(self.labelBehindButton[2], shapeMove)

        elif whichButton == 'B1':
            self.labelBehindButton[3].setGeometry(QtCore.QRect(250, 280, 71, 41))
            self.buttonMidLeft.deleteLater()
            self.buttonMidLeft = None
            self.show_move(self.labelBehindButton[3], shapeMove)

        elif whichButton == 'B2':
            self.labelBehindButton[4].setGeometry(QtCore.QRect(372, 280, 71, 41))
            self.buttonMidMid.deleteLater()
            self.buttonMidMid = None
            self.show_move(self.labelBehindButton[4], shapeMove)

        elif whichButton == 'B3':
            self.labelBehindButton[5].setGeometry(QtCore.QRect(493, 280, 71, 41))
            self.buttonMidRight.deleteLater()
            self.buttonMidRight = None
            self.show_move(self.labelBehindButton[5], shapeMove)

        elif whichButton == 'C1':
            self.labelBehindButton[6].setGeometry(QtCore.QRect(250, 370, 71, 41))
            self.buttonBottomLeft.deleteLater()
            self.buttonBottomLeft = None
            self.show_move(self.labelBehindButton[6], shapeMove)

        elif whichButton == 'C2':
            self.labelBehindButton[7].setGeometry(QtCore.QRect(370, 370, 71, 41))
            self.buttonBottomMid.deleteLater()
            self.buttonBottomMid = None
            self.show_move(self.labelBehindButton[7], shapeMove)

        elif whichButton == 'C3':
            self.labelBehindButton[8].setGeometry(QtCore.QRect(493, 370, 71, 41))
            self.buttonBottomRight.deleteLater()
            self.buttonBottomRight = None
            self.show_move(self.labelBehindButton[8], shapeMove)


    def show_move(self, whichLabel, whoMove):
        whichLabel.setAlignment(QtCore.Qt.AlignCenter)
        whichLabel.setText(QtCore.QCoreApplication.translate("mainWindow", whoMove))

    def who_move(self, whoMove):
        if whoMove:
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
    whoMove = True

    mainApplication = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(mainApplication.exec_())