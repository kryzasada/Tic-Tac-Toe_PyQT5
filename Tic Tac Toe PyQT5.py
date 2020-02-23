# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class UiMainWindow(object):
    def __init__(self):
        super(UiMainWindow, self).__init__()
        main_window.setObjectName('main_window')
        main_window.resize(800, 600)
        main_window.setWindowIcon(QtGui.QIcon('logo.png'))

        self.central_widget = QtWidgets.QWidget(main_window)

        self.line_horizontal_top = QtWidgets.QFrame(self.central_widget)
        self.line_horizontal_bottom = QtWidgets.QFrame(self.central_widget)
        self.line_upright_left = QtWidgets.QFrame(self.central_widget)
        self.line_upright_right = QtWidgets.QFrame(self.central_widget)

        self.font_label = QtGui.QFont()
        self.font_label.setPointSize(16)

        self.label_player_X = QtWidgets.QLabel(self.central_widget)
        self.label_player_O = QtWidgets.QLabel(self.central_widget)
        self.line_who_move = QtWidgets.QFrame(self.central_widget)

        self.label_behind_button = []

    def setup_ui(self, window):
        self.central_widget.setObjectName('central_widget')

        self.line_horizontal_top.setGeometry(QtCore.QRect(224, 242, 358, 16))
        self.line_horizontal_top.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horizontal_top.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_horizontal_bottom.setGeometry(QtCore.QRect(224, 342, 358, 16))
        self.line_horizontal_bottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horizontal_bottom.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_upright_left.setGeometry(QtCore.QRect(330, 170, 16, 261))
        self.line_upright_left.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_upright_left.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_upright_right.setGeometry(QtCore.QRect(470, 170, 16, 261))
        self.line_upright_right.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_upright_right.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.label_player_X.setGeometry(QtCore.QRect(210, 40, 131, 51))
        self.label_player_X.setFont(self.font_label)

        self.label_player_O.setGeometry(QtCore.QRect(480, 40, 131, 51))
        self.label_player_O.setFont(self.font_label)
        self.label_player_O.setObjectName('label_player_O')

        self.line_who_move.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_who_move.setLineWidth(1)

        self.who_move(who_move)

        self.font_label.setPointSize(10)
        for x in range(0, 9):
            self.label_behind_button.append(QtWidgets.QLabel(self.central_widget))
            self.label_behind_button[x].setFont(self.font_label)

        self.button_top_left = QtWidgets.QPushButton(self.central_widget)
        self.button_top_left.setGeometry(QtCore.QRect(250, 190, 71, 41))
        self.button_top_left.setText('')
        self.button_top_left.clicked.connect(lambda: self.connect_button('A1'))

        self.button_top_mid = QtWidgets.QPushButton(self.central_widget)
        self.button_top_mid.setGeometry(QtCore.QRect(370, 190, 71, 41))
        self.button_top_mid.setText('')
        self.button_top_mid.clicked.connect(lambda: self.connect_button('A2'))

        self.button_top_right = QtWidgets.QPushButton(self.central_widget)
        self.button_top_right.setGeometry(QtCore.QRect(493, 190, 71, 41))
        self.button_top_right.setText('')
        self.button_top_right.clicked.connect(lambda: self.connect_button('A3'))

        self.button_mid_left = QtWidgets.QPushButton(self.central_widget)
        self.button_mid_left.setGeometry(QtCore.QRect(250, 280, 71, 41))
        self.button_mid_left.setText('')
        self.button_mid_left.clicked.connect(lambda: self.connect_button('B1'))

        self.button_mid_mid = QtWidgets.QPushButton(self.central_widget)
        self.button_mid_mid.setGeometry(QtCore.QRect(372, 280, 71, 41))
        self.button_mid_mid.setText('')
        self.button_mid_mid.clicked.connect(lambda: self.connect_button('B2'))

        self.button_mid_right = QtWidgets.QPushButton(self.central_widget)
        self.button_mid_right.setGeometry(QtCore.QRect(493, 280, 71, 41))
        self.button_mid_right.setText('')
        self.button_mid_right.clicked.connect(lambda: self.connect_button('B3'))

        self.button_bottom_left = QtWidgets.QPushButton(self.central_widget)
        self.button_bottom_left.setGeometry(QtCore.QRect(250, 370, 71, 41))
        self.button_bottom_left.setText('')
        self.button_bottom_left.clicked.connect(lambda: self.connect_button('C1'))

        self.button_bottom_mid = QtWidgets.QPushButton(self.central_widget)
        self.button_bottom_mid.setGeometry(QtCore.QRect(370, 370, 71, 41))
        self.button_bottom_mid.setText('')
        self.button_bottom_mid.clicked.connect(lambda: self.connect_button('C2'))

        self.button_bottom_right = QtWidgets.QPushButton(self.central_widget)
        self.button_bottom_right.setGeometry(QtCore.QRect(493, 370, 71, 41))
        self.button_bottom_right.setText('')
        self.button_bottom_right.clicked.connect(lambda: self.connect_button('C3'))

        window.setCentralWidget(self.central_widget)

        self.retranslate_ui(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate('window', 'Tic-Tac-Toe'))
        self.label_player_X.setText(_translate('window', 'Player X = ' + str(score_player_X)))
        self.label_player_O.setText(_translate('window', 'Player O = ' + str(score_player_O)))

    def connect_button(self, which_button):
        global who_move
        global shape_move

        if who_move:
            shape_move = str('X')
            who_move = False
        else:
            shape_move = str('O')
            who_move = True

        self.who_move(who_move)

        if which_button == 'A1':
            self.label_behind_button[0].setGeometry(QtCore.QRect(250, 190, 71, 41))
            self.button_top_left.setVisible(False)
            self.show_move(self.label_behind_button[0], shape_move)

        elif which_button == 'A2':
            self.label_behind_button[1].setGeometry(QtCore.QRect(370, 190, 71, 41))
            self.button_top_mid.setVisible(False)
            self.show_move(self.label_behind_button[1], shape_move)

        elif which_button == 'A3':
            self.label_behind_button[2].setGeometry(QtCore.QRect(493, 190, 71, 41))
            self.button_top_right.setVisible(False)
            self.show_move(self.label_behind_button[2], shape_move)

        elif which_button == 'B1':
            self.label_behind_button[3].setGeometry(QtCore.QRect(250, 280, 71, 41))
            self.button_mid_left.setVisible(False)
            self.show_move(self.label_behind_button[3], shape_move)

        elif which_button == 'B2':
            self.label_behind_button[4].setGeometry(QtCore.QRect(372, 280, 71, 41))
            self.button_mid_mid.setVisible(False)
            self.show_move(self.label_behind_button[4], shape_move)

        elif which_button == 'B3':
            self.label_behind_button[5].setGeometry(QtCore.QRect(493, 280, 71, 41))
            self.button_mid_right.setVisible(False)
            self.show_move(self.label_behind_button[5], shape_move)

        elif which_button == 'C1':
            self.label_behind_button[6].setGeometry(QtCore.QRect(250, 370, 71, 41))
            self.button_bottom_left.setVisible(False)
            self.show_move(self.label_behind_button[6], shape_move)

        elif which_button == 'C2':
            self.label_behind_button[7].setGeometry(QtCore.QRect(370, 370, 71, 41))
            self.button_bottom_mid.setVisible(False)
            self.show_move(self.label_behind_button[7], shape_move)

        elif which_button == 'C3':
            self.label_behind_button[8].setGeometry(QtCore.QRect(493, 370, 71, 41))
            self.button_bottom_right.setVisible(False)
            self.show_move(self.label_behind_button[8], shape_move)

    def show_move(self, which_label, who_move_local):
        which_label.setAlignment(QtCore.Qt.AlignCenter)
        which_label.setText(QtCore.QCoreApplication.translate('main_window', who_move_local))
        self.check_win()

    def who_move(self, who_move_local):
        if who_move_local:
            self.line_who_move.setGeometry(QtCore.QRect(205, 58, 130, 51))
        else:
            self.line_who_move.setGeometry(QtCore.QRect(475, 58, 130, 51))

    def check_win(self):
        if ((self.label_behind_button[0].text() == shape_move and
                self.label_behind_button[1].text() == shape_move and
                self.label_behind_button[2].text() == shape_move) or
                (self.label_behind_button[3].text() == shape_move and
                 self.label_behind_button[4].text() == shape_move and
                 self.label_behind_button[5].text() == shape_move) or
                (self.label_behind_button[6].text() == shape_move and
                 self.label_behind_button[7].text() == shape_move and
                 self.label_behind_button[8].text() == shape_move) or

                (self.label_behind_button[0].text() == shape_move and
                 self.label_behind_button[3].text() == shape_move and
                 self.label_behind_button[6].text() == shape_move) or
                (self.label_behind_button[1].text() == shape_move and
                 self.label_behind_button[4].text() == shape_move and
                 self.label_behind_button[7].text() == shape_move) or
                (self.label_behind_button[2].text() == shape_move and
                 self.label_behind_button[5].text() == shape_move and
                 self.label_behind_button[8].text() == shape_move) or

                (self.label_behind_button[0].text() == shape_move and
                 self.label_behind_button[4].text() == shape_move and
                 self.label_behind_button[8].text() == shape_move) or
                (self.label_behind_button[2].text() == shape_move and
                 self.label_behind_button[4].text() == shape_move and
                 self.label_behind_button[6].text() == shape_move)):

            self.draw = 0
            window_win = QMessageBox()
            window_win.setWindowTitle('Won ' + shape_move)
            window_win.setText('Won player : ' + shape_move + '\n\n Play again? ')
            window_win.setIcon(QMessageBox.Information)
            window_win.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            window_win.buttonClicked.connect(self.check_win_QMessageBox)
            window_win.exec_()

        elif (self.label_behind_button[0].text() and self.label_behind_button[1].text() and
                self.label_behind_button[2].text() and self.label_behind_button[3].text() and
                self.label_behind_button[4].text() and self.label_behind_button[5].text() and
                self.label_behind_button[6].text() and self.label_behind_button[7].text() and
                self.label_behind_button[8].text()):

            self.draw = 1
            window_draw = QMessageBox()
            window_draw.setWindowTitle('Draw ')
            window_draw.setText('Draw \n\n Play again? ')
            window_draw.setIcon(QMessageBox.Information)
            window_draw.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            window_draw.buttonClicked.connect(self.check_win_QMessageBox)
            window_draw.exec_()

    def check_win_QMessageBox(self, i):
        if (i.text()) == '&Yes':
            self.button_top_left.setVisible(True)
            self.button_top_mid.setVisible(True)
            self.button_top_right.setVisible(True)
            self.button_mid_left.setVisible(True)
            self.button_mid_mid.setVisible(True)
            self.button_mid_right.setVisible(True)
            self.button_bottom_left.setVisible(True)
            self.button_bottom_mid.setVisible(True)
            self.button_bottom_right.setVisible(True)

            if (shape_move == 'X') and (self.draw != 1):
                global score_player_X
                score_player_X += 1
            elif (shape_move == 'O') and (self.draw != 1):
                global score_player_O
                score_player_O += 1

            self.retranslate_ui(main_window)

            for x in range(0, 9):
                self.label_behind_button[x].setText(QtCore.QCoreApplication.translate('main_window', ''))

        if (i.text()) == '&No':
            sys.exit()


if __name__ == "__main__":
    score_player_X = 0
    score_player_O = 0
    who_move = True

    main_application = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(main_application.exec_())