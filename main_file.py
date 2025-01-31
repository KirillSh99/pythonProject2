import sys
from PyQt5 import QtWidgets, QtCore, QtMultimedia, QtGui
from project_01 import MyWindow
from window_two import MyWindow_2
from information_file import MyWindow_information

app = QtWidgets. QApplication(sys. argv)
window = MyWindow()
window. setWindowFlags(QtCore. Qt. Window | QtCore. Qt. NoDropShadowWindowHint | QtCore. Qt. MSWindowsFixedSizeDialogHint)
window. windowType()

ico = QtGui. QIcon("n1.jpg")
window. setWindowIcon(ico)
app. setWindowIcon(ico)

oImage = QtGui.QImage("pic_2.jpg")
sImage = oImage.scaled(QtCore. QSize(785, 310))
palette = QtGui. QPalette()
palette.setBrush(QtGui. QPalette.Window, QtGui. QBrush(sImage))
window.setPalette(palette)

window. setWindowTitle('Notes')
window.setObjectName("MainCalculator")
window. resize(400, 550)
window. maps()

window_i = MyWindow_information()
window_i.setObjectName("MainInformation")

window_2 = MyWindow_2()
window_2.setObjectName("MainTwo")
# window. button()
# window. move(785, 310)


@QtCore.pyqtSlot()
def open_information():
    window_i.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.NoDropShadowWindowHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
    window_i.windowType()
    window_i.setWindowTitle('Information')
    window_i.bthQuit_ago_inf.setObjectName("Batter_ago_inf")
    window_i.resize(400, 550)

    rect = window.frameGeometry()

    window. close()

    @QtCore.pyqtSlot()
    def return_main_inf():
        rect_i = window_i.frameGeometry()
        window_i. close()
        window. move(rect_i.left(), rect_i.top())
        window. show()

    window_i. move(rect.left(), rect.top())
    window_i. show()
    window_i. bthQuit_ago_inf. clicked. connect(return_main_inf)


@QtCore.pyqtSlot()
def open_window_two():
    window_2.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.NoDropShadowWindowHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
    window_2.windowType()
    window_2.setWindowTitle('Your notes')
    window_2.bthQuit_ago.setObjectName("Batter_ago")
    window_2.bthQuit_adjust.setObjectName("Batter_adjust")
    window_2.bthQuit_save.setObjectName("Batter_save2")
    window_2.resize(400, 550)

    window_2.file = open('spicc.txt', encoding='utf-8')
    line = window_2.file.readline()
    window_2.notes_2 = ''
    while line:
        line = line.rstrip('\n')
        window_2.notes_2 += f'\n{line}'
        line = window_2.file.readline()

    window_2.textBrowser_2.setText(f'{window_2.notes_2}')

    rect = window.frameGeometry()

    window.close()

    @QtCore.pyqtSlot()
    def return_main_win2():
        rect_2 = window_2.frameGeometry()
        window_2. close()
        window.move(rect_2.left(), rect_2.top())
        window. show()

    window_2. move(rect.left(), rect.top())
    window_2. show()
    window_2. bthQuit_ago. clicked. connect(return_main_win2)

oImage_y = QtGui.QImage("pic_3.jpg")
sImage_y = oImage_y.scaled(QtCore. QSize(785, 310))
palette_y = QtGui. QPalette()
palette_y.setBrush(QtGui. QPalette.Window, QtGui. QBrush(sImage_y))

oImage_p = QtGui.QImage("pic_4n.jpg")
sImage_p = oImage_p.scaled(QtCore.QSize(400, 500))
palette_p = QtGui.QPalette()
palette_p.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage_p))

oImage_g = QtGui.QImage("pic_5.jpg")
sImage_g = oImage_g.scaled(QtCore. QSize(785, 310))
palette_g = QtGui. QPalette()
palette_g.setBrush(QtGui. QPalette.Window, QtGui. QBrush(sImage_g))

oImage_b = QtGui.QImage("pic_6.jpg")
sImage_b = oImage_b.scaled(QtCore. QSize(785, 310))
palette_b = QtGui. QPalette()
palette_b.setBrush(QtGui. QPalette.Window, QtGui. QBrush(sImage_b))


@QtCore.pyqtSlot()
def color_all():
    if window. count == 1:
        window.setPalette(palette_y)
        window_2.setPalette(palette_y)
        window_i.setPalette(palette_y)

        window.bthQuit_color_all.setText('Yellow')   # moccasin   khaki
        window.bthQuit_color_all.setStyleSheet('QPushButton#Color_all{background-color: #ffcc99; border-radius: 20px}'
                                               'QPushButton#Color_all:hover{background-color:yellow;}')

        window.bthQuit.setStyleSheet('QPushButton#Batter_close{background-color: moccasin; border-radius: 8px}'
                                     'QPushButton#Batter_close:hover{background-color:yellow;}')
        window.bthQuit_s.setStyleSheet('QPushButton#Batter_save{background-color: moccasin; border-radius: 8px}'
                                       'QPushButton#Batter_save:hover{background-color:yellow;}')
        window.bthQuit_new.setStyleSheet('QPushButton#Batter_new{background-color: moccasin; border-radius: 8px}'
                                         'QPushButton#Batter_new:hover{background-color:yellow;}')

        window_i.bthQuit_ago_inf.setStyleSheet('QPushButton#Batter_ago_inf{background-color: moccasin; border-radius: 8px}'
                                               'QPushButton#Batter_ago_inf:hover{background-color:yellow;}')

        window_2.bthQuit_ago.setStyleSheet('QPushButton#Batter_ago{background-color: moccasin; border-radius: 8px}'
                                           'QPushButton#Batter_ago:hover{background-color:yellow;}')
        window_2.bthQuit_adjust.setStyleSheet('QPushButton#Batter_adjust{background-color: moccasin; border-radius: 8px}'
                                              'QPushButton#Batter_adjust:hover{background-color:yellow;}')
        window_2.bthQuit_save.setStyleSheet('QPushButton#Batter_save2{background-color: moccasin; border-radius: 8px}'
                                            'QPushButton#Batter_save2:hover{background-color:yellow;}')

        window.bth_yournotes.setStyleSheet('QPushButton#Button_yournotes{background-color: khaki; border-radius: 20px}'
                                           'QPushButton#Button_yournotes:hover{background-color:yellow;}')
        window.bth_information.setStyleSheet('QPushButton#Button_information{background-color: khaki; border-radius: 8px}'
                                             'QPushButton#Button_information:hover{background-color:yellow;}')
        window.count += 1

    elif window. count == 2:
        window.setPalette(palette_p)
        window_2.setPalette(palette_p)
        window_i.setPalette(palette_p)

        window.bthQuit_color_all.setText('Barbie')   # pink  lightpink
        window.bthQuit_color_all.setStyleSheet('QPushButton#Color_all{background-color: plum; border-radius: 20px}'
                                               'QPushButton#Color_all:hover{background-color:yellow;}')

        window. media_player = QtMultimedia.QMediaPlayer()
        window. url = QtCore.QUrl.fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
        window. content = QtMultimedia.QMediaContent(window. url)
        window. media_player.setMedia(window. content)
        window. media_player.play()

        if window. count_textBrowser_time == 1:
            window.textBrowser_time.setObjectName("Text_time")
            window.textBrowser_time.setStyleSheet('QTextBrowser#Text_time{background-color: white; border-radius: 10px}')

        window.bthQuit.setStyleSheet('QPushButton#Batter_close{background-color: hotpink; border-radius: 8px}'
                                     'QPushButton#Batter_close:hover{background-color:yellow;}')
        window.bthQuit_s.setStyleSheet('QPushButton#Batter_save{background-color: hotpink; border-radius: 8px}'
                                       'QPushButton#Batter_save:hover{background-color:yellow;}')
        window.bthQuit_new.setStyleSheet('QPushButton#Batter_new{background-color: hotpink; border-radius: 8px}'
                                         'QPushButton#Batter_new:hover{background-color:yellow;}')
        window.textBrowser.setStyleSheet('QTextBrowser#Text{background-color: white; border-radius: 10px}')
        window.lable.setStyleSheet('QLabel#Label_window{color: white}')

        window_i.bthQuit_ago_inf.setStyleSheet('QPushButton#Batter_ago_inf{background-color: hotpink; border-radius: 8px}'
                                               'QPushButton#Batter_ago_inf:hover{background-color:yellow;}')
        window_i.textBrowser_3.setStyleSheet('QTextBrowser#Text_3{background-color: white; border-radius: 10px}')
        window_i.lable_i.setStyleSheet('QLabel#Label_window_i{color: white}')

        window_2.bthQuit_ago.setStyleSheet('QPushButton#Batter_ago{background-color: hotpink; border-radius: 8px}'
                                           'QPushButton#Batter_ago:hover{background-color:yellow;}')
        window_2.bthQuit_adjust.setStyleSheet('QPushButton#Batter_adjust{background-color: hotpink; border-radius: 8px}'
                                              'QPushButton#Batter_adjust:hover{background-color:yellow;}')
        window_2.bthQuit_save.setStyleSheet('QPushButton#Batter_save2{background-color: hotpink; border-radius: 8px}'
                                            'QPushButton#Batter_save2:hover{background-color:yellow;}')
        window_2.textBrowser_2.setStyleSheet('QTextBrowser#Text_2{background-color: white; border-radius: 10px}')
        window_2.lable_two.setStyleSheet('QLabel#Label_window_two{color: white}')

        window.bth_yournotes.setStyleSheet('QPushButton#Button_yournotes{background-color: pink; border-radius: 20px}'
                                           'QPushButton#Button_yournotes:hover{background-color:yellow;}')
        window.bth_information.setStyleSheet('QPushButton#Button_information{background-color: pink; border-radius: 8px}'
                                             'QPushButton#Button_information:hover{background-color:yellow;}')
        window. count += 1

    elif window. count == 3:
        window.setPalette(palette_g)
        window_2.setPalette(palette_g)
        window_i.setPalette(palette_g)

        window.bthQuit_color_all.setText('Green')   # yellowgreen   seagreen   green
        window.bthQuit_color_all.setStyleSheet('QPushButton#Color_all{background-color: gray; border-radius: 20px}'
                                               'QPushButton#Color_all:hover{background-color:yellow;}')

        window.media_player = QtMultimedia.QMediaPlayer()
        window.url = QtCore.QUrl.fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
        window.content = QtMultimedia.QMediaContent(window.url)
        window.media_player.setMedia(window.content)
        window.media_player.stop()

        window.bthQuit.setStyleSheet('QPushButton#Batter_close{background-color: green; border-radius: 8px}'
                                     'QPushButton#Batter_close:hover{background-color:yellow;}')
        window.bthQuit_s.setStyleSheet('QPushButton#Batter_save{background-color: green; border-radius: 8px}'
                                       'QPushButton#Batter_save:hover{background-color:yellow;}')
        window.bthQuit_new.setStyleSheet('QPushButton#Batter_new{background-color: green; border-radius: 8px}'
                                         'QPushButton#Batter_new:hover{background-color:yellow;}')
        window.textBrowser.setStyleSheet('QTextBrowser#Text{background-color: white; border-radius: 10px}')
        window.lable.setStyleSheet('QLabel#Label_window{color: white}')
        window. lable_3. setStyleSheet('QLabel#lable_3{color: white}')

        window_i.bthQuit_ago_inf.setStyleSheet('QPushButton#Batter_ago_inf{background-color: green; border-radius: 8px}'
                                               'QPushButton#Batter_ago_inf:hover{background-color:yellow;}')
        window_i.textBrowser_3.setStyleSheet('QTextBrowser#Text_3{background-color: white; border-radius: 10px}')
        window_i.lable_i.setStyleSheet('QLabel#Label_window_i{color: white}')

        window_2.bthQuit_ago.setStyleSheet('QPushButton#Batter_ago{background-color: green; border-radius: 8px}'
                                           'QPushButton#Batter_ago:hover{background-color:yellow;}')
        window_2.bthQuit_adjust.setStyleSheet('QPushButton#Batter_adjust{background-color: green; border-radius: 8px}'
                                              'QPushButton#Batter_adjust:hover{background-color:yellow;}')
        window_2.bthQuit_save.setStyleSheet('QPushButton#Batter_save2{background-color: green; border-radius: 8px}'
                                            'QPushButton#Batter_save2:hover{background-color:yellow;}')
        window_2.textBrowser_2.setStyleSheet('QTextBrowser#Text_2{background-color: white; border-radius: 10px}')
        window_2.lable_two.setStyleSheet('QLabel#Label_window_two{color: white}')

        window.bth_yournotes.setStyleSheet('QPushButton#Button_yournotes{background-color: seagreen; border-radius: 20px}'
                                           'QPushButton#Button_yournotes:hover{background-color:yellow;}')
        window.bth_information.setStyleSheet('QPushButton#Button_information{background-color: seagreen; border-radius: 8px}'
                                             'QPushButton#Button_information:hover{background-color:yellow;}')
        window. count += 1

    elif window. count == 4:
        window.setPalette(palette_b)
        window_2.setPalette(palette_b)
        window_i.setPalette(palette_b)

        window.bthQuit_color_all.setText('Blue')   # lightskyblue   cornflowerblue   lightsteelblue
        window.bthQuit_color_all.setStyleSheet('QPushButton#Color_all{background-color: cornflowerblue; border-radius: 20px}'
                                               'QPushButton#Color_all:hover{background-color:yellow;}')

        window.media_player = QtMultimedia.QMediaPlayer()
        window.url = QtCore.QUrl.fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
        window.content = QtMultimedia.QMediaContent(window.url)
        window.media_player.setMedia(window.content)
        window.media_player.stop()

        window.bthQuit.setStyleSheet('QPushButton#Batter_close{background-color: lightsteelblue; border-radius: 8px}'
                                     'QPushButton#Batter_close:hover{background-color:yellow;}')
        window.bthQuit_s.setStyleSheet('QPushButton#Batter_save{background-color: lightsteelblue; border-radius: 8px}'
                                       'QPushButton#Batter_save:hover{background-color:yellow;}')
        window.bthQuit_new.setStyleSheet('QPushButton#Batter_new{background-color: lightsteelblue; border-radius: 8px}'
                                         'QPushButton#Batter_new:hover{background-color:yellow;}')
        window.textBrowser.setStyleSheet('QTextBrowser#Text{background-color: white; border-radius: 10px}')
        window.lable.setStyleSheet('QLabel#Label_window{color: white}')
        window.lable_3.setStyleSheet('QLabel#lable_3{color: white}')

        window_i.bthQuit_ago_inf.setStyleSheet('QPushButton#Batter_ago_inf{background-color: lightsteelblue; border-radius: 8px}'
                                               'QPushButton#Batter_ago_inf:hover{background-color:yellow;}')
        window_i.textBrowser_3.setStyleSheet('QTextBrowser#Text_3{background-color: white; border-radius: 10px}')
        window_i.lable_i.setStyleSheet('QLabel#Label_window_i{color: white}')

        window_2.bthQuit_ago.setStyleSheet('QPushButton#Batter_ago{background-color: lightsteelblue; border-radius: 8px}'
                                           'QPushButton#Batter_ago:hover{background-color:yellow;}')
        window_2.bthQuit_adjust.setStyleSheet('QPushButton#Batter_adjust{background-color: lightsteelblue; border-radius: 8px}'
                                              'QPushButton#Batter_adjust:hover{background-color:yellow;}')
        window_2.bthQuit_save.setStyleSheet('QPushButton#Batter_save2{background-color: lightsteelblue; border-radius: 8px}'
                                            'QPushButton#Batter_save2:hover{background-color:yellow;}')
        window_2.textBrowser_2.setStyleSheet('QTextBrowser#Text_2{background-color: white; border-radius: 10px}')
        window_2.lable_two.setStyleSheet('QLabel#Label_window_two{color: white}')

        window.bth_yournotes.setStyleSheet('QPushButton#Button_yournotes{background-color: lightskyblue; border-radius: 20px}'
                                           'QPushButton#Button_yournotes:hover{background-color:yellow;}')
        window.bth_information.setStyleSheet('QPushButton#Button_information{background-color: lightskyblue; border-radius: 8px}'
                                             'QPushButton#Button_information:hover{background-color:yellow;}')
        window. count += 1

    else:
        window.setPalette(palette)
        window_2.setPalette(palette)
        window_i.setPalette(palette)

        if window. count_textBrowser_time == 1:
            window.textBrowser_time.setObjectName("Text_time")
            window.textBrowser_time.setStyleSheet('QTextBrowser#Text_time{background-color: #ffeedd; border-radius: 10px}')

        window.bthQuit_color_all.setText('Standard')   # orange
        window.bthQuit_color_all.setStyleSheet('QPushButton#Color_all{background-color: tan; border-radius: 20px}'
                                               'QPushButton#Color_all:hover{background-color:yellow;}')

        window.bthQuit.setStyleSheet('QPushButton#Batter_close{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                     'QPushButton#Batter_close:hover{background-color:yellow;}')
        window.bthQuit_s.setStyleSheet('QPushButton#Batter_save{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                       'QPushButton#Batter_save:hover{background-color:yellow;}')
        window.bthQuit_new.setStyleSheet('QPushButton#Batter_new{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                         'QPushButton#Batter_new:hover{background-color:yellow;}')
        window.textBrowser.setStyleSheet('QTextBrowser#Text{background-color: #ffeedd; border-radius: 10px}')
        window.lable.setStyleSheet('QLabel#Label_window{color: #330000}')
        window.lable_3.setStyleSheet('QLabel#lable_3{color: black}')

        window_i.bthQuit_ago_inf.setStyleSheet('QPushButton#Batter_ago_inf{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                               'QPushButton#Batter_ago_inf:hover{background-color:yellow;}')
        window_i.textBrowser_3.setStyleSheet('QTextBrowser#Text_3{background-color: #ffeedd; border-radius: 10px}')
        window_i.lable_i.setStyleSheet('QLabel#Label_window_i{color: #330000}')

        window_2.bthQuit_ago.setStyleSheet('QPushButton#Batter_ago{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                           'QPushButton#Batter_ago:hover{background-color:yellow;}')
        window_2.bthQuit_adjust.setStyleSheet('QPushButton#Batter_adjust{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                              'QPushButton#Batter_adjust:hover{background-color:yellow;}')
        window_2.bthQuit_save.setStyleSheet('QPushButton#Batter_save2{background-color: lightgoldenrodyellow; border-radius: 8px}'
                                            'QPushButton#Batter_save2:hover{background-color:yellow;}')
        window_2.textBrowser_2.setStyleSheet('QTextBrowser#Text_2{background-color: #ffeedd; border-radius: 10px}')
        window_2.lable_two.setStyleSheet('QLabel#Label_window_two{color: #330000}')

        window.bth_yournotes.setStyleSheet('QPushButton#Button_yournotes{background-color: wheat; border-radius: 20px}'
                                           'QPushButton#Button_yournotes:hover{background-color:yellow;}')
        window.bth_information.setStyleSheet('QPushButton#Button_information{background-color: wheat; border-radius: 8px}'
                                             'QPushButton#Button_information:hover{background-color:yellow;}')
        window.count = 1

# def color_one():
#     window. media_player = QtMultimedia.QMediaPlayer()
#     window. url = QtCore.QUrl.fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
#     window. content = QtMultimedia.QMediaContent(window. url)
#     window. media_player.setMedia(window. content)
#     window. media_player.play()
#
#     window. setStyleSheet("#MainCalculator{background-color: pink}")
#     window.bthQuit.setStyleSheet("#Batter_close{background-color: hotpink}")
#     window.bthQuit_s.setStyleSheet("#Batter_save{background-color: hotpink}")
#     window.bthQuit_new.setStyleSheet("#Batter_new{background-color: hotpink}")
#
#     window_i.setStyleSheet("#MainInformation{background-color: pink}")
#     window_i.bthQuit_ago_inf.setStyleSheet("#Batter_ago_inf{background-color: hotpink}")
#
#     window_2.setStyleSheet("#MainTwo{background-color: pink}")
#     window_2.bthQuit_ago.setStyleSheet("#Batter_ago{background-color: hotpink}")
#     window_2.bthQuit_adjust.setStyleSheet("#Batter_adjust{background-color: hotpink}")
#     window_2.bthQuit_save.setStyleSheet("#Batter_save2{background-color: hotpink}")

# def color_two():
#     window. media_player = QtMultimedia.QMediaPlayer()
#     window. url = QtCore.QUrl.fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
#     window. content = QtMultimedia.QMediaContent(window. url)
#     window. media_player.setMedia(window. content)
#     window. media_player.stop()
#
#     window.setStyleSheet("#MainCalculator{background-color: yellowgreen}")
#     window.bthQuit.setStyleSheet("#Batter_close{background-color: green}")
#     window.bthQuit_s.setStyleSheet("#Batter_save{background-color: green}")
#     window.bthQuit_new.setStyleSheet("#Batter_new{background-color: green}")
#
#     window_i.setStyleSheet("#MainInformation{background-color: yellowgreen}")
#     window_i.bthQuit_ago_inf.setStyleSheet("#Batter_ago_inf{background-color: green}")
#
#     window_2.setStyleSheet("#MainTwo{background-color: yellowgreen}")
#     window_2.bthQuit_ago.setStyleSheet("#Batter_ago{background-color: green}")
#     window_2.bthQuit_adjust.setStyleSheet("#Batter_adjust{background-color: green}")
#     window_2.bthQuit_save.setStyleSheet("#Batter_save2{background-color: green}")

# def color_three():
#     window. media_player = QtMultimedia.QMediaPlayer()
#     window. url = QtCore.QUrl.fromLocalFile("Dua_Lipa_-_Dance_The_Night_76056639.mp3")
#     window. content = QtMultimedia.QMediaContent(window. url)
#     window. media_player.setMedia(window. content)
#     window. media_player.stop()
#
#     window.setStyleSheet("#MainCalculator{background-color: lightskyblue}")
#     window.bthQuit.setStyleSheet("#Batter_close{background-color: cornflowerblue}")
#     window.bthQuit_s.setStyleSheet("#Batter_save{background-color: cornflowerblue}")
#     window.bthQuit_new.setStyleSheet("#Batter_new{background-color: cornflowerblue}")
#
#     window_i.setStyleSheet("#MainInformation{background-color: lightskyblue}")
#     window_i.bthQuit_ago_inf.setStyleSheet("#Batter_ago_inf{background-color: cornflowerblue}")
#
#     window_2.setStyleSheet("#MainTwo{background-color: lightskyblue}")
#     window_2.bthQuit_ago.setStyleSheet("#Batter_ago{background-color: cornflowerblue}")
#     window_2.bthQuit_adjust.setStyleSheet("#Batter_adjust{background-color: cornflowerblue}")
#     window_2.bthQuit_save.setStyleSheet("#Batter_save2{background-color: cornflowerblue}")

def button():
    window. bthQuit_color_all = QtWidgets.QPushButton(window)
    window. bthQuit_color_all. setText('Application themes')
    window.bthQuit_color_all.setGeometry(QtCore.QRect(13, 487, 270, 59))
    window. bthQuit_color_all. setObjectName("Color_all")

    # window.bthColor_one = QtWidgets.QPushButton(window)
    # window.bthColor_one.setText('Barbie')
    # window.bthColor_one.setGeometry(QtCore.QRect(13, 487, 59, 59))
    # window.bthColor_one.setObjectName("Color_one")
    # window.bthColor_one.setStyleSheet("#Color_one{background-color: plum}")
    # window.bthColor_two = QtWidgets.QPushButton(window)
    # window.bthColor_two.setGeometry(QtCore.QRect(107, 487, 59, 59))
    # window.bthColor_two.setObjectName("Color_two")
    # window.bthColor_two.setStyleSheet("#Color_two{background-color: seagreen}")
    # window.bthColor_three = QtWidgets.QPushButton(window)
    # window.bthColor_three.setGeometry(QtCore.QRect(201, 487, 59, 59))
    # window.bthColor_three.setObjectName("Color_three")
    # window.bthColor_three.setStyleSheet("#Color_three{background-color: lightsteelblue}")
    window.bth_yournotes = QtWidgets.QPushButton(window)
    window.bth_yournotes.setText('Your\n notes')
    window.bth_yournotes.setGeometry(QtCore.QRect(327, 487, 59, 59))
    window.bth_yournotes.setObjectName("Button_yournotes")
    window.bth_information = QtWidgets.QPushButton(window)
    window.bth_information.setText('I')
    window.bth_information.setGeometry(QtCore.QRect(295, 487, 30, 59))
    window.bth_information.setObjectName("Button_information")

    window.bthQuit_color_all.setStyleSheet('QPushButton#Color_all{background-color: tan; border-radius: 20px}'
                                           'QPushButton#Color_all:hover{background-color:yellow;}')
    window.bth_yournotes.setStyleSheet('QPushButton#Button_yournotes{background-color: wheat; border-radius: 20px}'
                                       'QPushButton#Button_yournotes:hover{background-color:yellow;}')
    window.bth_information.setStyleSheet('QPushButton#Button_information{background-color: wheat; border-radius: 8px}'
                                         'QPushButton#Button_information:hover{background-color:yellow;}')

    window.vbox_2 = QtWidgets.QVBoxLayout()
    # window.vbox_2.addWidget(window.bthColor_one)
    # window.vbox_2.addWidget(window.bthColor_two)
    # window.vbox_2.addWidget(window.bthColor_three)
    window.vbox_2.addWidget(window.bth_yournotes)
    window.vbox_2.addWidget(window.bth_information)
    window. vbox_2. addWidget(window. bthQuit_color_all)
    window.setLayout(window.vbox_2)

    # window.bthColor_one.clicked.connect(color_one)
    # window.bthColor_two.clicked.connect(color_two)
    # window.bthColor_three.clicked.connect(color_three)
    window.bth_information.clicked.connect(open_information)
    window.bth_yournotes.clicked.connect(open_window_two)
    window. bthQuit_color_all. clicked. connect(color_all)

button()
window. show()

sys. exit(app. exec_())