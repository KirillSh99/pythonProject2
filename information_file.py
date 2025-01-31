import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class MyWindow_information(QtWidgets. QWidget):
    def __init__(self, parent = None):
        QtWidgets. QWidget. __init__(self, parent)

        oImage_i = QtGui.QImage("pic_2.jpg")
        sImage_i = oImage_i.scaled(QtCore.QSize(785, 310))
        palette_i = QtGui.QPalette()
        palette_i.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage_i))
        self.setPalette(palette_i)

        self. lable_i = QtWidgets. QLabel('<center><h3>Information</center></h3>\n_____________________________________________________')
        self.lable_i.setObjectName("Label_window_i")
        self.lable_i.setStyleSheet('QLabel#Label_window_i{color: #330000}')

        self. textBrowser_3 = QtWidgets. QTextBrowser()
        self.textBrowser_3.setObjectName("Text_3")
        self.textBrowser_3.setStyleSheet('QTextBrowser#Text_3{background-color: #ffeedd; border-radius: 10px}')
        self. textBrowser_3.setText('Информация по эксплуатации приложения.\n'
                                    '1. Кнопки приложения.\n2. Эксплуатация заметок.')

        self. bthQuit_ago_inf = QtWidgets. QPushButton('ago')
        self. bthQuit_ago_inf. setObjectName("Batter_ago_inf")
        self. bthQuit_ago_inf. setStyleSheet('QPushButton#Batter_ago_inf{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                             'QPushButton#Batter_ago_inf:hover{background-color:yellow;}')

        self. vbox_3 = QtWidgets. QVBoxLayout()
        self. vbox_3. addWidget(self. lable_i)
        self. vbox_3. addWidget(self. textBrowser_3)
        self. vbox_3. addWidget(self. bthQuit_ago_inf)
        self. setLayout(self. vbox_3)