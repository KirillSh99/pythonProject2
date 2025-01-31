import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class MyWindow_2(QtWidgets. QWidget):
    def __init__(self, parent = None):
        QtWidgets. QWidget. __init__(self, parent)

        oImage_2 = QtGui.QImage("pic_2.jpg")
        sImage_2 = oImage_2.scaled(QtCore.QSize(785, 310))
        palette_2 = QtGui.QPalette()
        palette_2.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage_2))
        self.setPalette(palette_2)

        self. notes_new = ''
        self. lable_two = QtWidgets. QLabel('<center><h3>Your notes</center></h3>\n_____________________________________________________')
        self.lable_two.setObjectName("Label_window_two")
        self.lable_two.setStyleSheet('QLabel#Label_window_two{color: #330000}')

        self. textBrowser_2 = QtWidgets. QTextBrowser()
        self.textBrowser_2.setObjectName("Text_2")
        self.textBrowser_2.setStyleSheet('QTextBrowser#Text_2{background-color: #ffeedd; border-radius: 10px}')
        # self. file = open('spicc.txt', encoding='utf-8')
        # # self. window. file = open('C:/Users/ksepi/OneDrive/Рабочий стол/text', 'r', encoding='utf-8')
        # # self.window.file = open('C:/Users/ksepi/OneDrive/Рабочий стол/text', encoding='utf-8')
        # line = self. file. readline()
        # self. notes_2 = ''
        # while line:
        #     line = line.rstrip('\n')
        #     self. notes_2 += f'\n{line}'
        #     line = self. file. readline()
        #
        # self. textBrowser_2. setText(f'{self. notes_2}')
        # print(self. window. new)

        self. bthQuit_ago = QtWidgets. QPushButton('ago')
        self. bthQuit_ago. setObjectName("Batter_ago")
        self. bthQuit_adjust = QtWidgets. QPushButton('adjust')
        self. bthQuit_adjust. setObjectName("Batter_adjust")
        self. bthQuit_save = QtWidgets. QPushButton('save changes')
        self. bthQuit_save. setObjectName("Batter_save2")
        self. bthQuit_save. setStyleSheet("#Batter_save2{background-color: gray}")

        self. bthQuit_ago. setStyleSheet('QPushButton#Batter_ago{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                         'QPushButton#Batter_ago:hover{background-color:yellow;}')
        self.bthQuit_adjust.setStyleSheet('QPushButton#Batter_adjust{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                          'QPushButton#Batter_adjust:hover{background-color:yellow;}')
        self.bthQuit_save.setStyleSheet('QPushButton#Batter_save2{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                        'QPushButton#Batter_save2:hover{background-color:yellow;}')

        self. vbox_3 = QtWidgets. QVBoxLayout()
        self. vbox_3. addWidget(self. lable_two)
        self. vbox_3. addWidget(self. textBrowser_2)
        self. vbox_3. addWidget(self. bthQuit_adjust)
        self. vbox_3. addWidget(self. bthQuit_save)
        self. vbox_3. addWidget(self. bthQuit_ago)
        self. setLayout(self. vbox_3)

        self. bthQuit_adjust. clicked. connect(self. adjust)
        self. bthQuit_save. clicked. connect(self. again_save)

    @QtCore.pyqtSlot()
    def adjust(self):
        self.textBrowser_2. setReadOnly(False)

    @QtCore.pyqtSlot()
    def again_save(self):
        self. notes_new = self. textBrowser_2. toPlainText()

        self.file = open('spicc.txt', 'w', encoding='utf-8')
        self.file.write(f'{self.notes_new}\n')
        self.file.close()

        self.textBrowser_2.setReadOnly(True)