# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class Ui_mainWindow(object):


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)

        self.labelBehindButton = []

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")




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

        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelPlayerX = QtWidgets.QLabel(self.centralwidget)
        self.labelPlayerX.setGeometry(QtCore.QRect(210, 40, 131, 51))
        self.labelPlayerX.setFont(font)
        self.labelPlayerX.setObjectName("labelPlayerX")

        self.labelPlayerY = QtWidgets.QLabel(self.centralwidget)
        self.labelPlayerY.setGeometry(QtCore.QRect(480, 40, 131, 51))
        self.labelPlayerY.setFont(font)
        self.labelPlayerY.setObjectName("labelPlayerY")

        self.lineWhoMove = QtWidgets.QFrame(self.centralwidget)
        self.lineWhoMove.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineWhoMove.setLineWidth(1)

        self.who_move(whoMove)

        font.setPointSize(10)
        for x in range(0, 9):
            self.labelBehindButton.append(QtWidgets.QLabel(self.centralwidget))
            self.labelBehindButton[x].setFont(font)

        self.buttonTopLeft = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTopLeft.setGeometry(QtCore.QRect(250, 190, 71, 41))
        self.buttonTopLeft.setText("")
        self.buttonTopLeft.clicked.connect(lambda: self.connect_button("A1"))

        self.buttonTopMid = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTopMid.setGeometry(QtCore.QRect(370, 190, 71, 41))
        self.buttonTopMid.setText("")
        self.buttonTopMid.clicked.connect(lambda: self.connect_button("A2"))

        self.buttonTopRight = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTopRight.setGeometry(QtCore.QRect(493, 190, 71, 41))
        self.buttonTopRight.setText("")
        self.buttonTopRight.clicked.connect(lambda: self.connect_button("A3"))



        self.buttonMidLeft = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMidLeft.setGeometry(QtCore.QRect(250, 280, 71, 41))
        self.buttonMidLeft.setText("")
        self.buttonMidLeft.clicked.connect(lambda: self.connect_button("B1"))

        self.buttonMidMid = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMidMid.setGeometry(QtCore.QRect(372, 280, 71, 41))
        self.buttonMidMid.setText("")
        self.buttonMidMid.clicked.connect(lambda: self.connect_button("B2"))

        self.buttonMidRight = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMidRight.setGeometry(QtCore.QRect(493, 280, 71, 41))
        self.buttonMidRight.setText("")

        self.buttonMidRight.clicked.connect(lambda: self.connect_button("B3"))



        self.buttonBottomLeft = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBottomLeft.setGeometry(QtCore.QRect(250, 370, 71, 41))
        self.buttonBottomLeft.setText("")
        self.buttonBottomLeft.clicked.connect(lambda: self.connect_button("C1"))

        self.buttonBottomMid = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBottomMid.setGeometry(QtCore.QRect(370, 370, 71, 41))
        self.buttonBottomMid.setText("")
        self.buttonBottomMid.clicked.connect(lambda: self.connect_button("C2"))

        self.buttonBottomRight = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBottomRight.setGeometry(QtCore.QRect(493, 370, 71, 41))
        self.buttonBottomRight.setText("")
        self.buttonBottomRight.clicked.connect(lambda: self.connect_button("C3"))


        mainWindow.setCentralWidget(self.centralwidget)


        self.retranslate_Ui(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslate_Ui(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Tic-Tac-Toe"))
        self.labelPlayerX.setText(_translate("mainWindow", "Player X = " + str(scoreX)))
        self.labelPlayerY.setText(_translate("mainWindow", "Player O = " + str(scoreY)))


    def connect_button(self, whichButton):
        global whoMove
        global shapeMove

        if whoMove :
            shapeMove = str('X')
            whoMove = False
        else:
            shapeMove = str("O")
            whoMove = True


        self.who_move(whoMove)

        if whichButton == 'A1':
            self.labelBehindButton[0].setGeometry(QtCore.QRect(250, 190, 71, 41))
            self.buttonTopLeft.setVisible(False)
            self.show_move(self.labelBehindButton[0], shapeMove)

        elif whichButton == 'A2':
            self.labelBehindButton[1].setGeometry(QtCore.QRect(370, 190, 71, 41))
            self.buttonTopMid.setVisible(False)
            self.show_move(self.labelBehindButton[1], shapeMove)

        elif whichButton == 'A3':
            self.labelBehindButton[2].setGeometry(QtCore.QRect(493, 190, 71, 41))
            self.buttonTopRight.setVisible(False)
            self.show_move(self.labelBehindButton[2], shapeMove)

        elif whichButton == 'B1':
            self.labelBehindButton[3].setGeometry(QtCore.QRect(250, 280, 71, 41))
            self.buttonMidLeft.setVisible(False)
            self.show_move(self.labelBehindButton[3], shapeMove)

        elif whichButton == 'B2':
            self.labelBehindButton[4].setGeometry(QtCore.QRect(372, 280, 71, 41))
            self.buttonMidMid.setVisible(False)
            self.show_move(self.labelBehindButton[4], shapeMove)

        elif whichButton == 'B3':
            self.labelBehindButton[5].setGeometry(QtCore.QRect(493, 280, 71, 41))
            self.buttonMidRight.setVisible(False)
            self.show_move(self.labelBehindButton[5], shapeMove)

        elif whichButton == 'C1':
            self.labelBehindButton[6].setGeometry(QtCore.QRect(250, 370, 71, 41))
            self.buttonBottomLeft.setVisible(False)
            self.show_move(self.labelBehindButton[6], shapeMove)

        elif whichButton == 'C2':
            self.labelBehindButton[7].setGeometry(QtCore.QRect(370, 370, 71, 41))
            self.buttonBottomMid.setVisible(False)
            self.show_move(self.labelBehindButton[7], shapeMove)

        elif whichButton == 'C3':
            self.labelBehindButton[8].setGeometry(QtCore.QRect(493, 370, 71, 41))
            self.buttonBottomRight.setVisible(False)
            self.show_move(self.labelBehindButton[8], shapeMove)



    def show_move(self, whichLabel, whoMove):
        whichLabel.setAlignment(QtCore.Qt.AlignCenter)
        whichLabel.setText(QtCore.QCoreApplication.translate("mainWindow", whoMove))
        self.check_win()


    def who_move(self, whoMove):
        if whoMove:
            self.lineWhoMove.setGeometry(QtCore.QRect(205, 58, 130, 51))
        else:
            self.lineWhoMove.setGeometry(QtCore.QRect(475, 58, 130, 51))


    def check_win(self):
        if (((self.labelBehindButton[0].text() == shapeMove) and (self.labelBehindButton[1].text() == shapeMove) and
                 (self.labelBehindButton[2].text() == shapeMove)) or
                ((self.labelBehindButton[3].text() == shapeMove) and (self.labelBehindButton[4].text() == shapeMove) and
                 (self.labelBehindButton[5].text() == shapeMove)) or
                ((self.labelBehindButton[6].text() == shapeMove) and (self.labelBehindButton[7].text() == shapeMove) and
                 (self.labelBehindButton[8].text() == shapeMove)) or

                ((self.labelBehindButton[0].text() == shapeMove) and (self.labelBehindButton[3].text() == shapeMove) and
                 (self.labelBehindButton[6].text() == shapeMove)) or
                ((self.labelBehindButton[1].text() == shapeMove) and (self.labelBehindButton[4].text() == shapeMove) and
                 (self.labelBehindButton[7].text() == shapeMove)) or
                ((self.labelBehindButton[2].text() == shapeMove) and (self.labelBehindButton[5].text() == shapeMove) and
                 (self.labelBehindButton[8].text() == shapeMove)) or

                ((self.labelBehindButton[0].text() == shapeMove) and (self.labelBehindButton[4].text() == shapeMove) and
                 (self.labelBehindButton[8].text() == shapeMove)) or
                ((self.labelBehindButton[2].text() == shapeMove) and (self.labelBehindButton[4].text() == shapeMove) and
                 (self.labelBehindButton[6].text() == shapeMove))):

            self.draw = 0
            windowWin = QMessageBox()
            windowWin.setWindowTitle("Won " + shapeMove)
            windowWin.setText("Won player : " + shapeMove + "\n\n Play again? ")
            windowWin.setIcon(QMessageBox.Information)
            windowWin.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            windowWin.buttonClicked.connect(self.check_win_QMessageBox)
            windowWin.exec_()

        elif ((self.labelBehindButton[0].text()) and (self.labelBehindButton[1].text()) and
                (self.labelBehindButton[2].text()) and (self.labelBehindButton[3].text()) and
                (self.labelBehindButton[4].text()) and (self.labelBehindButton[5].text()) and
                (self.labelBehindButton[6].text()) and (self.labelBehindButton[7].text()) and
                (self.labelBehindButton[8].text())):

            self.draw = 1
            windowWin = QMessageBox()
            windowWin.setWindowTitle("Draw ")
            windowWin.setText("Draw \n\n Play again? ")
            windowWin.setIcon(QMessageBox.Information)
            windowWin.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            windowWin.buttonClicked.connect(self.check_win_QMessageBox)
            windowWin.exec_()

    def check_win_QMessageBox(self, i):
        if (i.text()) == '&Yes':
            self.buttonTopLeft.setVisible(True)
            self.buttonTopMid.setVisible(True)
            self.buttonTopRight.setVisible(True)
            self.buttonMidLeft.setVisible(True)
            self.buttonMidMid.setVisible(True)
            self.buttonMidRight.setVisible(True)
            self.buttonBottomLeft.setVisible(True)
            self.buttonBottomMid.setVisible(True)
            self.buttonBottomRight.setVisible(True)

            if (shapeMove == 'X') and  (self.draw != 1):
                global scoreX
                scoreX += 1
            elif (shapeMove == 'O') and (self.draw != 1):
                global scoreY
                scoreY += 1

            self.retranslate_Ui(mainWindow)

            for x in range(0, 9):
                self.labelBehindButton[x].setText(QtCore.QCoreApplication.translate("mainWindow", ""))

        if (i.text()) == '&No':
            sys.exit()
            #mainApplication.quit()






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