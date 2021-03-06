import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from Ui_Form import Ui_MainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy
from pygame import mixer
class Beg(QtWidgets.QWidget):   #Основное окно где будут отображаться все действия
    def __init__(self):
        super().__init__()
        self.kli = QLabel(self)
        self.n = 'Тест_1'
        self.n2 = 'Тест_2'
        self.n3 = 'Тест_3'
        self.n4 = 'Тест_4'
        self.n5 = 'Тест_5'
        self.secondWin = None
        self.initUI()
    def initUI(self):
        nach = QPushButton('Начать')
        beg = QPushButton('Позорно сбежать')
        beg.clicked.connect(QCoreApplication.instance().quit)
        #nach.clicked.connect(self.openWin)
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(nach, 1, 0)
        grid.addWidget(beg, 1, 1)
        nach.clicked.connect(self.run)
        self.setLayout(grid)
        self.resize(450, 350)
        self.center()
        self.setWindowTitle('Начало близко!')
        self.show()
    def run(self):
        self.i, okBtnPressed = QInputDialog.getText(
            self, "Возьминете ответственность", "Как вас зовут?"
        )
        if okBtnPressed:
            self.kli.setText(self.i)
        self.openWin()
    def openWin(self): #Открытие второго окна
        if not self.secondWin:
            self.secondWin = SecondWindow(self, self.n, self.n2, self.n3, self.n4, self.n5, self.i)
        self.secondWin.show()
        self.hide()
    def closeEvent(self, event): #Вопрос о закрытие окна через крестик
        reply = QMessageBox.question(self, 'Message', "Товарищь, не совершай ошибок!!",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
class SecondWindow(QtWidgets.QWidget): #Все тесты
    def __init__(self, n="Тест_1",  n1="Тест_1", n2="Тест_2", n3='Тест_3', n4='Тест_4', n5='Тест_5', i = 'etlid', parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.n4 = n4
        self.n = n1
        self.n2 = n2
        self.n3 = n3
        self.n5 = n5
        self.i = i
        self.f1Win = None
        self.build()
    def build(self):
        self.but1 = QPushButton(str(self.n), self)
        self.but2 = QPushButton(str(self.n2), self)
        self.but3 = QPushButton(str(self.n3), self)
        self.but4 = QPushButton(str(self.n4), self)
        self.but5 = QPushButton(str(self.n5), self)
        self.itog = QPushButton('Подвести Итоги!!', self)
        grid = QGridLayout()
        grid.setSpacing(10)
        self.but1.clicked.connect(self.test1)
        self.but2.clicked.connect(self.test2)
        self.but3.clicked.connect(self.test3)
        self.but4.clicked.connect(self.test4)
        self.but5.clicked.connect(self.test5)
        self.itog.clicked.connect(self.podv)
        grid.addWidget(self.but1, 1, 1)
        grid.addWidget(self.but2, 2, 1)
        grid.addWidget(self.but3, 3, 1)
        grid.addWidget(self.but4, 4, 1)
        grid.addWidget(self.but5, 5, 1)
        grid.addWidget(self.itog, 6, 1)
        self.setLayout(grid)
        self.resize(450, 350)
        self.center()
        self.setWindowTitle('Выбирай!')
        self.show()
    def test1(self): #Открытие первого теста
        self.f1Win1 = FirstTest(self, self.n2, self.n3, self.n4, self.n5, self.i)
        self.f1Win1.show()
        self.hide()
    def test2(self):
        self.f1Win2 = SecondTest(self, self.n, self.n3, self.n4, self.n5, self.i)
        self.f1Win2.show()
        self.hide()
    def test3(self):
        self.f1Win3 = ThirdTest(self, self.n, self.n2, self.n4, self.n5, self.i)
        self.f1Win3.show()
        self.hide()
    def test4(self):
        self.f1Win4 = FourthTest(self, self.n, self.n2, self.n3, self.n5, self.i)
        self.f1Win4.show()
        self.hide()
    def test5(self):
        self.f1Win5 = FifthTest(self, self.n, self.n2, self.n3, self.n4, self.i)
        self.f1Win5.show()
        self.hide()
    def podv(self):
        if self.n == 'Тест_1' and self.n2 == 'Тест_2' and  self.n3 == "Тест_3" and self.n4 == 'Тест_4' and self.n5 == 'Тест_5':
            i, okBtnPressed = QInputDialog.getItem(self, "Выбирай с умом!", "Ты еще не исполнил сое предназначение!", ("Вернуться и закончить тест", "Вернуться и закончить тест"), 1, False)
            if i == "Вернуться и закончить тест":
                pass
        else:
            self.f1Win6 = LastW(self, self.n, self.n2, self.n3, self.n4, self.n5, self.i)
            self.f1Win6.show()
            self.hide()
    def closeEvent(self, event):  # Вопрос о закрытие окна через крестик
        reply = QMessageBox.question(self, 'Message', "Товарищь, не совершай ошибок!!",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
class FirstTest(QtWidgets.QWidget):
    def __init__(self, n='Тест_1', n2='Тест_2', n3="Тест_3", n4='Тест_4', n5='Тест_5', i='', parent=None):
        super().__init__()
        self.test ='Верно!'
        self.build()
        self.i = i
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
    def build(self):
        self.text = ("Настало время, дети мои. Пришло время исполнить предназначение, встать бок о бок, и дать отпор злобным тварям, порожденым самыми темными уголками безумного разума создателя этого теста."
                     "Ходят легенды, что он до сих пор ходит в поисках кофе и ищет потерянную оптимизации, там где её отродясь не было. Так востаньте же дети мои, и начните свой крестовый поход. А вот и первое испытание - Нажмите кнопку R")
        self.label = QtWidgets.QLabel(self.text)
        self.label.setWordWrap(True)
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)
        self.resize(450, 350)
        self.center()
        self.show()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_R:
            self.n1 = 'Верно'
            self.w2 = SecondWindow('Teст_1', 'Начало положено!', self.n2, self.n3, self.n4, self.n5, self.i)
            self.hide()
    def closeEvent(self, event): #Вопрос о закрытие окна через крестик
        reply = QMessageBox.question(self, 'Message', "Товарищь, не совершай ошибок!!",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
class SecondTest(QtWidgets.QWidget):
    def __init__(self, n="Тест_1", n1='Тест_1', n3='Тест_3', n4='Тест_4', n5='Тест_5', i='', parent=None):
        super().__init__()
        self.i = i
        self.n1 = n1
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.build()
    def build(self):
        self.text = ("ВЫ выпустили первого всадника багов! Маленкую, незаментную запятую, которая рушит плоды многочасовых работ и бессонных ночей. Кучи скрюченных за компом тел закричали от ужаса. По их венам полился первобытный страх."
                     " И только великий ctrl + **&^ может спасти нас, но найдетё ли вы истинное лицо этого героя, или вам суждено блуждать в ротемках?")
        self.but = QPushButton('Выбрать', self)
        self.but.clicked.connect(self.Chois)
        self.label = QtWidgets.QLabel(self.text)
        self.label.setWordWrap(True)
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.label, 1, 1)
        grid.addWidget(self.but, 2, 1)
        self.setLayout(grid)
        self.resize(450, 350)
        self.center()
        self.show()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_R:
            self.hide()
    def Chois(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Выбирай с умом!",
            "Найди Истину",
            ("ctrl + x", "ctrl + z", "ctrl + c", "ctrl + v"),
            1,
            False
        )
        if i == "ctrl + z":
            self.w2 = SecondWindow('Teст_1', self.n1, 'И был он избран что бы видеть истину!', self.n3, self.n4, self.n5, self.i)
            self.hide()
        else:
            self.w2 = SecondWindow('Teст_1', self.n1, 'Ты был близок, но великие сервера решили иначе!', self.n3, self.n4, self.n5, self.i)
            self.hide()
    def closeEvent(self, event): #Вопрос о закрытие окна через крестик
        reply = QMessageBox.question(self, 'Message', "Товарищь, не совершай ошибок!!",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
class ThirdTest(QtWidgets.QWidget):
    def __init__(self, n="Тест_1", n1='Тест_1', n2='Тест_2', n4='Тест_4', n5='Тест_5', i='', parent=None):
        super().__init__()
        self.test ='Верно!'
        self.i = i
        self.n1 = n1
        self.n2 = n2
        self.n4 = n4
        self.n5 = n5
        self.build()
    def build(self):
        self.text = ("Но вот перед нами предстали вестники смерти алгоритма всетворящего, те кто оптимизировать его пытался, и те кто погрязая в разрушение кода, продолжали нести свое зло. НО вот встретили они последника создателя великого, и спросили: "
                     "В чём смысл кода данного?")
        self.labl = QLabel(self)
        pixmap = QPixmap('vs.jpeg')
        self.labl.setPixmap(pixmap)
        self.kil = QPushButton('Дерзныть узнать в чем смысл творения этого!', self)
        self.sav = QPushButton('Ливнуть из чата, убегая от ужасов закоулок разума чужеродного!', self)
        self.kil.clicked.connect(self.mess)
        self.sav.clicked.connect(self.vos)
        self.label = QtWidgets.QLabel(self.text)
        self.label.setWordWrap(True)
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.labl, 1, 1)
        grid.addWidget(self.label, 2, 1)
        grid.addWidget(self.kil, 3, 1)
        grid.addWidget(self.sav, 4, 1)
        self.setLayout(grid)
        self.resize(450, 350)
        self.center()
        self.show()
    def vos(self):
        self.w2 = SecondWindow('Teст_1', self.n1, self.n2, 'Вы сохранили свой разум, но потеряли нечто другое', self.n4, self.n5, self.i)
        self.hide()
    def mess(self):
        i, okBtnPressed = QInputDialog.getItem  (
            self, "Не Надо ", "ВЫ УВЕРЕНЫ?", ("Да", "Нет", "Да нет наверное"), 1, False)
        if i == "Да":
            self.mess1()
        else:
            self.w2 = SecondWindow('Teст_1', self.n1, self.n2, 'Вы сохранили свой разум, но потеряли нечто другое', self.n4, self.n5, self.i)
            self.hide()
    def mess1(self):
        i1, okBtnPressed = QInputDialog.getItem(
            self, "Не Надо ", "ВЫ ТОЧНО УВЕРЕНЫ?", ("ДА", "Нууу...Нет", "Да нет наверное"), 1, False)
        if i1 == "ДА":
            self.mess2()
        else:
            self.w2 = SecondWindow('Teст_1', self.n1, self.n2, 'Вы сохранили свой разум, но потеряли нечто другое', self.n4, self.n5, self.i)
            self.hide()
    def mess2(self):
        i2, okBtnPressed = QInputDialog.getItem(
            self, "МОНСТР", "ВЫ ТОЧНО УВЕРЕНЫ?", ("ДА", "Нет, боже, НЕТ", "Да нет наверное"), 1, False)
        if i2 == "ДА":
            self.w2 = SecondWindow('Teст_1', self.n1, self.n2, 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ', self.n4, self.n5, self.i)
        else:
            self.w2 = SecondWindow('Teст_1', self.n1, self.n2, 'Вы сохранили свой разум, но потеряли нечто другое', self.n4, self.n5, self.i)
        self.hide()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_R:
            self.hide()
    def closeEvent(self, event): #Вопрос о закрытие окна через крестик
        reply = QMessageBox.question(self, 'Message', "Товарищь, не совершай ошибок!!",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
class FourthTest(QMainWindow, Ui_MainWindow):
    def __init__(self, n='Тест_1', n1="Тест_1", n2="Тест_2", n3='Тест_3', n5='Тест_5', i='', parent=None):
        super().__init__()
        self.i = i
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n5 = n5
        self.o = 0
        self.setupUi(self)
        self.center()
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.otv)
    def run(self):
        if self.radioButton.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(10)],
                             [i for i in range(10)],
                             pen='r')
            self.o = 1
        elif self.radioButton_2.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(10)],
                             [i + 100 for i in range(10)],
                             pen='g')
            self.o = 2
        elif self.radioButton_3.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(10)],
                             [-i - 100 for i in range(10)],
                             pen='b')
            self.o = 3
    def otv(self):
        if self.o == 1 or self.o == 3:
            self.w2 = SecondWindow('Teст_1', self.n1, self.n2, self.n3, 'Вам неудолось осознать неосозноваемое ', self.n5, self.i)
            self.w2.show()
            self.hide()
        elif self.o == 2:
            self.w2 = SecondWindow('Teст_1', self.n1, self.n2, self.n3, 'Теперь вы нечто большее, чем просто человек', self.n5, self.i)
            self.hide()
    def closeEvent(self, event): #Вопрос о закрытие окна через крестик
        reply = QMessageBox.question(self, 'Message', "Товарищь, не совершай ошибок!!",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
class FifthTest(QtWidgets.QWidget):
    def __init__(self, n="Тест_1", n1='Тест_1', n2='Тест_2', n3='Тест_3', n4='Тест_4', i='', parent=None):
        self.my_counter = 1
        self.i = i
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        QWidget.__init__(self)
        self.label = QLabel("Прокликанно:", self)
        self.text = ("А теперь, настало время показать предел своих возможностей, найти ту границу и сломать её, переступить свой предел и прокликать 50 раз за 10 секунд!")
        self.vop = QtWidgets.QLabel(self.text)
        self.vop.setWordWrap(True)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.button = QPushButton("Кликай!", self)
        self.button.clicked.connect(self.button_handler)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 2, 1)
        self.layout.addWidget(self.button, 3, 1)
        self.layout.addWidget(self.vop, 1, 1)
        self.setLayout(self.layout)
        self.resize(450, 350)
        self.center()
        self.show()
        self.build()
    def build(self):
        self.timer = QTimer()
        self.timer.start(15000)
        self.timer.timeout.connect(self.exite)
    def exite(self):
        self.w2 = SecondWindow('Teст_1', self.n1, self.n2, self.n3, self.n4, 'Я не тормоз, я медленный газ!', self.i)
        self.timer.stop()
        self.hide()
    def pobeda(self):
        self.w2 = SecondWindow('Teст_1', self.n1, self.n2, self.n3, self.n4, 'Удачных выплат штрафов за превышения скорости!', self.i)
        self.timer.stop()
        self.hide()
    def button_handler(self):
        self.label.setText("Qlabel" + " %d tick" % self.my_counter)
        self.my_counter += 1
        if self.my_counter == 51:
            self.pobeda()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_R:
            self.hide()
    def closeEvent(self, event): #Вопрос о закрытие окна через крестик
        reply = QMessageBox.question(self, 'Message', "Товарищь, не совершай ошибок!!",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
class LastW(QtWidgets.QWidget):
    def __init__(self, n, n1, n2, n3, n4, n5, i, parent=None):
        super().__init__()
        self.i = str(i)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.build()
    def build(self):
        self.resize(450, 350)
        self.nam = QLabel(self.i)
        self.text = ("Поздравляю, ! Вы прошли этот тест!")
        self.label = QtWidgets.QLabel(self.text)
        self.label.setWordWrap(True)
        grid = QGridLayout()
        grid.setSpacing(10)
        if self.n2 == 'И был он избран что бы видеть истину!' and self.n3 == 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 == 'Теперь вы нечто большее, чем просто человек' and self.n5 == 'Удачных выплат штрафов за превышения скорости!':
            self.labl = QLabel(self)
            pixmap = QPixmap('v1.jpeg')
            self.labl.setPixmap(pixmap)
            mixer.init()
            mixer.music.load('r1.mp3')
            mixer.music.play()
            self.text1 = ("Вы достигли высоты просветления, очистили разум, поняли непостигаемое... Короче ващ IQ over99999, и даже не спрашивайте по какой системе мы это высчитывали!")
            self.ra = QtWidgets.QLabel(self.text1)
            self.ra.setWordWrap(True)
        elif (self.n2 == 'И был он избран что бы видеть истину!' and self.n3 == 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 == 'Теперь вы нечто большее, чем просто человек' and self.n5 != 'Удачных выплат штрафов за превышения скорости!')\
              or (self.n2 != 'И был он избран что бы видеть истину!' and self.n3 == 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 == 'Теперь вы нечто большее, чем просто человек' and self.n5 == 'Удачных выплат штрафов за превышения скорости!')\
              or (self.n2 == 'И был он избран что бы видеть истину!' and self.n3 != 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 == 'Теперь вы нечто большее, чем просто человек' and self.n5 == 'Удачных выплат штрафов за превышения скорости!')\
              or (self.n2 == 'И был он избран что бы видеть истину!' and self.n3 == 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 != 'Теперь вы нечто большее, чем просто человек' and self.n5 == 'Удачных выплат штрафов за превышения скорости!'):
            self.labl = QLabel(self)
            pixmap = QPixmap('v2.jpeg')
            self.labl.setPixmap(pixmap)
            mixer.init()
            mixer.music.load('r2.mp3')
            mixer.music.play()
            self.text1 = ("Вы были близки, но оступились")
            self.ra = QtWidgets.QLabel(self.text1)
            self.ra.setWordWrap(True)
        elif (self.n2 != 'И был он избран что бы видеть истину!' and self.n3 != 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 == 'Теперь вы нечто большее, чем просто человек' and self.n5 == 'Удачных выплат штрафов за превышения скорости!')\
            or (self.n2 != 'И был он избран что бы видеть истину!' and self.n3 == 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 != 'Теперь вы нечто большее, чем просто человек' and self.n5 == 'Удачных выплат штрафов за превышения скорости!')\
            or (self.n2 != 'И был он избран что бы видеть истину!' and self.n3 == 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 == 'Теперь вы нечто большее, чем просто человек' and self.n5 != 'Удачных выплат штрафов за превышения скорости!')\
            or (self.n2 == 'И был он избран что бы видеть истину!' and self.n3 != 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 != 'Теперь вы нечто большее, чем просто человек' and self.n5 == 'Удачных выплат штрафов за превышения скорости!')\
            or (self.n2 == 'И был он избран что бы видеть истину!' and self.n3 != 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 == 'Теперь вы нечто большее, чем просто человек' and self.n5 != 'Удачных выплат штрафов за превышения скорости!') \
            or (self.n2 == 'И был он избран что бы видеть истину!' and self.n3 == 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 != 'Теперь вы нечто большее, чем просто человек' and self.n5 != 'Удачных выплат штрафов за превышения скорости!'):
            self.labl = QLabel(self)
            pixmap = QPixmap('v3.jpeg')
            self.labl.setPixmap(pixmap)
            mixer.init()
            mixer.music.load('r3.mp3')
            mixer.music.play()
            self.text1 = ("Вы прошли вссего лишь пол пути... Или же целых пол пути?...")
            self.ra = QtWidgets.QLabel(self.text1)
            self.ra.setWordWrap(True)
        elif (self.n2 != 'И был он избран что бы видеть истину!' and self.n3 != 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 != 'Теперь вы нечто большее, чем просто человек' and self.n5 == 'Удачных выплат штрафов за превышения скорости!')\
            or (self.n2 != 'И был он избран что бы видеть истину!' and self.n3 != 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 == 'Теперь вы нечто большее, чем просто человек' and self.n5 != 'Удачных выплат штрафов за превышения скорости!')\
            or (self.n2 != 'И был он избран что бы видеть истину!' and self.n3 == 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 != 'Теперь вы нечто большее, чем просто человек' and self.n5 != 'Удачных выплат штрафов за превышения скорости!')\
            or (self.n2 == 'И был он избран что бы видеть истину!' and self.n3 != 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 != 'Теперь вы нечто большее, чем просто человек' and self.n5 != 'Удачных выплат штрафов за превышения скорости!'):
            self.labl = QLabel(self)
            pixmap = QPixmap('v4.jpeg')
            self.labl.setPixmap(pixmap)
            mixer.init()
            mixer.music.load('r5.mp3')
            mixer.music.play()
            self.text1 = ("Вы двигались в правильную сторону, к несчатью, не долго...")
            self.ra = QtWidgets.QLabel(self.text1)
            self.ra.setWordWrap(True)
        elif self.n2 != 'И был он избран что бы видеть истину!' and self.n3 != 'Вам открылся секрет чужого кода, вам, но не вашуму разуму ' and self.n4 != 'Теперь вы нечто большее, чем просто человек' and self.n5 != 'Удачных выплат штрафов за превышения скорости!':
            self.labl = QLabel(self)
            pixmap = QPixmap('v5.jpeg')
            self.labl.setPixmap(pixmap)
            mixer.init()
            mixer.music.load('r4.mp3')
            mixer.music.play()
            self.text1 = ("Ты запутался... серьезно запутался... КРАЙНЕ серьезно запутался")
            self.ra = QtWidgets.QLabel(self.text1)
            self.ra.setWordWrap(True)
        grid.addWidget(self.nam, 1, 1)
        grid.addWidget(self.label, 2, 1)
        grid.addWidget(self.labl, 4, 1)
        grid.addWidget(self.ra, 3, 1)
        self.setLayout(grid)
        self.center()
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Beg()
    sys.exit(app.exec_())