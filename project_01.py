import sys
from PyQt5 import QtWidgets, QtCore, QtMultimedia
import time, datetime
from functools import lru_cache
from plyer import notification
from window_two import MyWindow_2
from information_file import MyWindow_information

class MyWindow(QtWidgets. QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget. __init__(self, parent)
        self. window_2 = MyWindow_2()
        self. window_i = MyWindow_information()

        self. lable = QtWidgets. QLabel('<center><h3>Notes</center></h3>\n_____________________________________________________')
        self.lable.setObjectName("Label_window")
        self. lable. setStyleSheet('QLabel#Label_window{color: #330000}')
        self. lable_2 = QtWidgets. QLabel('\n \n')
        self. lable_3 = QtWidgets. QLabel("")
        self.lable_3.setObjectName("lable_3")
        # self. lable_3. setAlignment(QtCore.Qt.AlignHCenter)

        self. bthQuit = QtWidgets. QPushButton('close window')
        self. bthQuit. setObjectName("Batter_close")
        self. bthQuit_s = QtWidgets. QPushButton('save note')
        self.bthQuit_s.setObjectName("Batter_save")
        self. bthQuit_new = QtWidgets. QPushButton('new note')
        self.bthQuit_new.setObjectName("Batter_new")

        self. bthQuit. setStyleSheet('QPushButton#Batter_close{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                     'QPushButton#Batter_close:hover{background-color:yellow;}')
        self.bthQuit_s.setStyleSheet('QPushButton#Batter_save{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                     'QPushButton#Batter_save:hover{background-color:yellow;}')
        self.bthQuit_new.setStyleSheet('QPushButton#Batter_new{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                       'QPushButton#Batter_new:hover{background-color:yellow;}')

        self. textBrowser = QtWidgets. QTextBrowser(self)
        self.textBrowser.setObjectName("Text")
        self.textBrowser.setStyleSheet('QTextBrowser#Text{background-color: #ffeedd; border-radius: 10px}')
        self. textBrowser. setReadOnly(False)

        self. vbox = QtWidgets. QVBoxLayout()
        self. vbox. addWidget(self.lable_3)
        self. vbox. addWidget(self. lable)
        self. vbox. addWidget(self. textBrowser)
        self. vbox. addWidget(self. bthQuit)
        self. vbox. addWidget(self. bthQuit_s)
        self. vbox. addWidget(self. bthQuit_new)
        self. vbox. addWidget(self. lable_2)
        self. setLayout(self. vbox)

        self. bthQuit. clicked. connect(QtWidgets. qApp. quit)
        self. bthQuit_s. clicked. connect(self. save)
        self. bthQuit_new. clicked. connect(self. new_note)

        self.timer = QtCore.QTimer()
        self.timer.start(500)
        self.timer.timeout.connect(self.on_timeout)

        self. note = ''
        self. note_time = ''
        self. count = 1
        self. count_time = 1
        self.count_window_size = 1
        self. window_all = 1
        self. close_event = 0
        self. count_textBrowser_time = 0

    def on_timeout(self):
        self. lable_3. setText(time. strftime("%H:%M:%S    %d.%m.%Y"))

        # self. file_time = open('your_time.txt', 'a', encoding='utf-8')
        # line_time = self. file_time. readline()
        # self. ans_note_time = ''
        # while line_time:
        #     line_time = line_time.rstrip('\n')
        #     if time. strftime("%H:%M:%S    %d.%m.%Y") == '23:00:00    21.11.2023':
        #         notification.notify(message='Программа выполнена успешно', app_name='script', title='Готово')

    @lru_cache(maxsize=None)
    def maps(self):
        desktop = QtWidgets. QApplication. desktop()
        x = (desktop. width() - self. width()) // 2
        y = (desktop. height() - self. height()) // 2
        self. move(x, y)

    @QtCore.pyqtSlot()
    def save(self):
        if len(self. textBrowser.toPlainText()) != 0:
            self. note = self. textBrowser. toPlainText()

            # self.file = open('C:/Users/ksepi/OneDrive/Рабочий стол/text', 'a', encoding='utf-8')
            self. file = open('spicc.txt', 'a', encoding='utf-8')
            # self. file = open('C:/Users/ksepi/OneDrive/Рабочий стол/text', 'a+', encoding='utf-8')
            self. file. write('--------------------------------------------------------------------')
            self. file. write(f'\n{self. note}\n\n')
            self. file. write(f'                                                                     {datetime.date. today()}')
            self. file. close()

            self.textBrowser.setReadOnly(True)
            self. textBrowser. setText('<center><h3 style="color:#07f71f">Your note is save !</center></h3>')
            self. bthQuit_s. setDisabled(True)

        # elif len(self. textBrowser.toPlainText()) != 0 and len(self. textBrowser_time.toPlainText()) != 0:
        #     self. note_time = self. textBrowser_time. toPlainText()
        #     self. note = self. textBrowser. toPlainText()
        #
        #     self. file_time = open('your_time.txt', 'a', encoding='utf-8')
        #     self. file_time. write(f'{self. note_time}\n')
        #     self. file_time. close()
        #
        #     self. file_your_time = open(f'{self. note_time}.txt', 'a', encoding='utf-8')
        #     self. file_time. write(f'{self. note}')
        #     self. file_your_time. close()

        else:
            self.textBrowser.setReadOnly(True)
            self.textBrowser.setText('<center><h3 style="color:#f70707">You did not write down a single note !</center></h3>')
            self.bthQuit_s.setDisabled(True)

    @QtCore.pyqtSlot()
    def new_note(self):
        self.textBrowser.setReadOnly(False)
        self.bthQuit_s.setDisabled(False)
        self. textBrowser. setText('')

    def event(self, e):
        if e. type() == QtCore. QEvent. KeyPress:
            if e. text() == 'K' and self. textBrowser. toPlainText() == 'SH':
                self. close_event += 1
                self.textBrowser.setReadOnly(True)
                self.textBrowser.setText('<center><h3 style="color:yellow">Вы в режиме администратора !\n'
                                         'Приветствуем вас Шепитько Кирилл !</center></h3>')

                self.bthQuit_admin = QtWidgets.QPushButton('T')
                self. bthQuit_admin. setObjectName('Admin')
                self.bthQuit_admin1 = QtWidgets.QPushButton('S')
                self.bthQuit_admin2 = QtWidgets.QPushButton('A')
                self.bthQuit_admin3 = QtWidgets.QPushButton()
                self.bthQuit_admin4 = QtWidgets.QPushButton()

                self. bthQuit_admin. setFixedSize(30, 30)
                self.bthQuit_admin1.setFixedSize(30, 30)
                self.bthQuit_admin2.setFixedSize(30, 30)
                self.bthQuit_admin3.setFixedSize(30, 30)
                self.bthQuit_admin4.setFixedSize(30, 30)

                self. hbox = QtWidgets. QHBoxLayout()
                self. hbox. addWidget(self. bthQuit_admin)
                self.hbox.addStretch(1)
                self.hbox.addWidget(self.bthQuit_admin1)
                self.hbox.addStretch(1)
                self.hbox.addWidget(self.bthQuit_admin2)
                self.hbox.addStretch(1)
                self.hbox.addWidget(self.bthQuit_admin3)
                self.hbox.addStretch(1)
                self.hbox.addWidget(self.bthQuit_admin4)

                self.vbox.addLayout(self.hbox)
                self.vbox.addWidget(self.lable_2)
                self. bthQuit_admin. clicked. connect(self. button_admin)
                self.bthQuit_admin1.clicked. connect(self.button_admin1)
                self.bthQuit_admin2.clicked. connect(self.button_admin2)

            elif e. text() == 'T':
                global textBrowser_time

                self. count_textBrowser_time = 1
                self.close_event += 2

                self.textBrowser_time = QtWidgets.QTextBrowser(self)
                self.textBrowser_time.setObjectName("Text_time")
                if self. count == 5 or self. count == 1:
                    self.textBrowser_time.setStyleSheet('QTextBrowser#Text_time{background-color: #ffeedd; border-radius: 10px}')
                else:
                    self.textBrowser_time.setStyleSheet('QTextBrowser#Text_time{background-color: white; border-radius: 10px}')
                self.textBrowser_time.setReadOnly(False)
                self. textBrowser_time. setFixedSize(372, 30)

                # self.hbox.deleteLater()

                self.vbox.addWidget(self.lable)
                self.vbox.addWidget(self.textBrowser_time)
                self.vbox.addWidget(self.textBrowser)
                self.vbox.addWidget(self.bthQuit)
                self.vbox.addWidget(self.bthQuit_s)
                self.vbox.addWidget(self.bthQuit_new)
                # self.vbox.addLayout(self.hbox)
                self.vbox.addWidget(self.lable_2)

            elif e. text() == 'K' and self. textBrowser. toPlainText() == 'END':
                if self. close_event == 0:
                    pass
                elif self. close_event == 1:
                    self. bthQuit_admin. deleteLater()
                    self.bthQuit_admin1.deleteLater()
                    self.bthQuit_admin2.deleteLater()
                    self.bthQuit_admin3.deleteLater()
                    self.bthQuit_admin4.deleteLater()

                    self. hbox. deleteLater()
                    self.textBrowser.setText('')
                    self.window_2.close()
                    self.window_i.close()
                elif self. close_event == 2:
                    self.textBrowser_time.deleteLater()
                    self.textBrowser.setText('')
                else:
                    self.bthQuit_admin.deleteLater()
                    self.bthQuit_admin1.deleteLater()
                    self.bthQuit_admin2.deleteLater()
                    self.bthQuit_admin3.deleteLater()
                    self.bthQuit_admin4.deleteLater()
                    self.textBrowser_time.deleteLater()
                    self.hbox.deleteLater()
                    self.textBrowser.setText('')
                    self.window_2.close()
                    self.window_i.close()

                self. close_event = 0
                self. count_textBrowser_time = 0

        return QtWidgets. QWidget. event(self, e)

    @QtCore.pyqtSlot()
    def button_admin(self):
        if self. count_time == 1:
            self. lable_3. setStyleSheet('QLabel#lable_3{color: black}')
            self.bthQuit_admin.setStyleSheet('QPushButton#Admin{background-color: black; border-radius: 8px}'
                                             'QPushButton#Admin:hover{background-color:yellow;}')
            self. count_time += 1
        elif self. count_time == 2:
            self.lable_3.setStyleSheet('QLabel#lable_3{color: white}')
            self.bthQuit_admin.setStyleSheet('QPushButton#Admin{background-color: white; border-radius: 8px}'
                                             'QPushButton#Admin:hover{background-color:yellow;}')
            self.count_time = 1

    @QtCore.pyqtSlot()
    def button_admin1(self):
        if self. count_window_size == 1:
            self. bthQuit_admin1. setText('Max')
            self. showMaximized()
            self. count_window_size += 1
        elif self. count_window_size == 2:
            self.bthQuit_admin1.setText('N')
            self.showNormal()
            self.count_window_size += 1
        elif self. count_window_size == 3:
            self.bthQuit_admin1.setText('Min')
            self.showMinimized()
            self.count_window_size = 1

    @QtCore.pyqtSlot()
    def button_admin2(self):
        if self. window_all == 1:
            self. rect = self.frameGeometry()

            self. window_2. show()
            self. window_2.setWindowTitle('Your notes')
            self. window_2.move(self. rect.left() - 500, self. rect.top())
            self. window_2.resize(400, 550)
            self. window_2.file = open('spicc.txt', encoding='utf-8')
            line = self. window_2.file.readline()
            self. window_2.notes_2 = ''
            while line:
                line = line.rstrip('\n')
                self. window_2.notes_2 += f'\n{line}'
                line = self. window_2.file.readline()

            self. window_2.textBrowser_2.setText(f'{self. window_2.notes_2}')

            self. window_i. show()
            self. window_i.setWindowTitle('Information')
            self. window_i.move(self.rect.left() + 500, self.rect.top())
            self. window_i.resize(400, 550)

            self. window_all += 1
        elif self. window_all == 2:
            self. window_2. close()
            self. window_i. close()
            self. window_all = 1


    # def color_one(self):
    #     self. media_player = QtMultimedia. QMediaPlayer()
    #     self. url = QtCore. QUrl. fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
    #     self. content = QtMultimedia. QMediaContent(self. url)
    #     self. media_player.setMedia(self. content)
    #     self. media_player. play()
    #
    #     self. setStyleSheet("#MainCalculator{background-color: pink}")
    #     self.bthQuit.setStyleSheet("#Batter_close{background-color: hotpink}")
    #     self.bthQuit_s.setStyleSheet("#Batter_save{background-color: hotpink}")
    #     self.bthQuit_new.setStyleSheet("#Batter_new{background-color: hotpink}")
    #
    # def color_two(self):
    #     self.media_player = QtMultimedia.QMediaPlayer()
    #     self.url = QtCore.QUrl.fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
    #     self.content = QtMultimedia.QMediaContent(self.url)
    #     self.media_player.setMedia(self.content)
    #     self.media_player.stop()
    #
    #     self.setStyleSheet("#MainCalculator{background-color: yellowgreen}")
    #     self.bthQuit.setStyleSheet("#Batter_close{background-color: green}")
    #     self.bthQuit_s.setStyleSheet("#Batter_save{background-color: green}")
    #     self.bthQuit_new.setStyleSheet("#Batter_new{background-color: green}")
    #
    # def color_three(self):
    #     self.media_player = QtMultimedia.QMediaPlayer()
    #     self.url = QtCore.QUrl.fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
    #     self.content = QtMultimedia.QMediaContent(self.url)
    #     self.media_player.setMedia(self.content)
    #     self.media_player.stop()
    #
    #     self.setStyleSheet("#MainCalculator{background-color: lightskyblue}")
    #     self.bthQuit.setStyleSheet("#Batter_close{background-color: cornflowerblue}")
    #     self.bthQuit_s.setStyleSheet("#Batter_save{background-color: cornflowerblue}")
    #     self.bthQuit_new.setStyleSheet("#Batter_new{background-color: cornflowerblue}")
    #
    # # def information(self):
    # #     self.media_player = QtMultimedia.QMediaPlayer()
    # #     self.url = QtCore.QUrl.fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
    # #     self.content = QtMultimedia.QMediaContent(self.url)
    # #     self.media_player.setMedia(self.content)
    # #     self.media_player.stop()
    # #
    # #     self.bthQuit_s.setDisabled(True)
    # #
    # #     self. setStyleSheet("#MainCalculator{background-color: orange}")
    # #     self.bthQuit.setStyleSheet("#Batter_close{background-color: gray}")
    # #     self.bthQuit_s.setStyleSheet("#Batter_save{background-color: gray}")
    # #     self.bthQuit_new.setStyleSheet("#Batter_new{background-color: gray}")
    # #     self.textBrowser.setText('Информация по эксплуатации приложения.\n'
    # #                              '1. Кнопки приложения.\n2. Эксплуатация заметок.')
    #
    # def button(self):
    #     self. bthColor_one = QtWidgets. QPushButton(self)
    #     self. bthColor_one. setText('Barbie')
    #     self. bthColor_one. setGeometry(QtCore. QRect(13, 487, 59, 59))
    #     self. bthColor_one.setObjectName("Color_one")
    #     self. bthColor_one.setStyleSheet("#Color_one{background-color: plum}")
    #     self. bthColor_two = QtWidgets.QPushButton(self)
    #     self. bthColor_two.setGeometry(QtCore.QRect(107, 487, 59, 59))
    #     self. bthColor_two.setObjectName("Color_two")
    #     self. bthColor_two.setStyleSheet("#Color_two{background-color: seagreen}")
    #     self. bthColor_three = QtWidgets.QPushButton(self)
    #     self. bthColor_three.setGeometry(QtCore.QRect(201, 487, 59, 59))
    #     self. bthColor_three.setObjectName("Color_three")
    #     self. bthColor_three.setStyleSheet("#Color_three{background-color: lightsteelblue}")
    #     self. bth_yournotes = QtWidgets.QPushButton(self)
    #     self. bth_yournotes. setText('Your\n notes')
    #     self. bth_yournotes. setGeometry(QtCore.QRect(327, 487, 59, 59))
    #     self. bth_yournotes.setObjectName("Button_yournotes")
    #     self. bth_yournotes.setStyleSheet("#Button_yournotes{background-color: gray}")
    #     self.bth_information = QtWidgets.QPushButton(self)
    #     self.bth_information.setText('I')
    #     self.bth_information.setGeometry(QtCore.QRect(295, 487, 30, 59))
    #     self.bth_information.setObjectName("Button_information")
    #     self.bth_information.setStyleSheet("#Button_information{background-color: gray}")
    #
    #     self. vbox_2 = QtWidgets. QVBoxLayout()
    #     self. vbox_2. addWidget(self. bthColor_one)
    #     self. vbox_2. addWidget(self. bthColor_two)
    #     self.vbox_2.addWidget(self.bthColor_three)
    #     self. vbox_2. addWidget(self. bth_yournotes)
    #     self.vbox_2.addWidget(self.bth_information)
    #     self. setLayout(self. vbox_2)
    #
    #     self.bthColor_one.clicked.connect(self.color_one)
    #     self. bthColor_two. clicked. connect(self. color_two)
    #     self.bthColor_three. clicked. connect(self. color_three)
        #--------------------------------------------------------
        # self.bth_information. clicked. connect(self. information)
        # self. bth_yournotes. clicked. connect(QtWidgets. qApp. quit)

# class SlotWindow(QtCore. QObject):
#     def __init__(self, parent = None):
#         QtCore. QObject.__init__(self, parent)
#
#     @QtCore.pyqtSlot()
#     def new_note(self):
#         self.textBrowser.setReadOnly(False)
#         self.bthQuit_s.setDisabled(False)
#         self. textBrowser. setText('')
#
# obj = SlotWindow()