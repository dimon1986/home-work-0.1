import sys
import random

from M_Dawson_Home_Work.Chapter_2.QtPy5.challenge_QtPy2_1_2_Ui import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowTitle('Щедрый посетитель & блюдо')
        self.setWindowIcon(QIcon('data/waiter'))
        # тут будут храниться слова блюд
        self.list_str = []
        # создаю картеж чек боксов, для разной фигни
        self.carton_box = (self.checkBox_0, self.checkBox_1, self.checkBox_2,
                           self.checkBox_3, self.checkBox_4, self.checkBox_5,
                           self.checkBox_6, self.checkBox_7, self.checkBox_8, self.checkBox_9)
        for checkbox in self.carton_box:
            checkbox.stateChanged.connect(self.myfunction)

        @self.pushButton.clicked.connect
        def click():
            # передаём число сколько рондомить
            self.functionbutton(2)
        # любой подходящий сигнал будет работать
        self.radioButton_0.clicked.connect(self.onchecked)
        self.radioButton_1.released.connect(self.onchecked)
        self.radioButton_2.clicked.connect(self.onchecked)

    def myfunction(self, state):
        """функция которая добавляет или удаляет слова
        в список"""
        def words_w():
            # подфункция для вписания слов
            words = ''.join(self.list_str)
            self.textEdit.setText(words)
        sender = self.sender()  # определяем источник сигнала с помощью метода sender()
        if state == Qt.Checked:  # если нажали
            self.list_str.append(sender.text())
            words_w()
        else:
            self.list_str.remove(sender.text())
            words_w()

    def functionbutton(self, digit):
        """родномит выбор из чекбоксов"""
        for j in range(digit):
            for checkbox in random.choices(self.carton_box):
                checkbox.toggle()

    def onchecked(self):
        """меняет картинку и делает расчет с последующей вставкой"""
        try:
            bill = int(self.lineEdit_2.text())
            if bill > 0:
                sender = self.sender()
                if sender.text() == '20% чаявых' and bill:
                    self.label_3.setText('Итого: ' + str(bill*1.2))
                    self.label_waiter.setPixmap(QtGui.QPixmap('data/waiter_0.png'))
                elif sender.text() == '15% чаявых' and bill:
                    self.label_3.setText('Итого: ' + str(bill * 1.15))
                    self.label_waiter.setPixmap(QtGui.QPixmap('data/waiter_1.png'))
                else:
                    self.label_3.setText('Итого: ' + str(bill))
                    self.label_waiter.setPixmap(QtGui.QPixmap('data/waiter_2.png'))
            else:
                self.label_3.setText('Пожалуйста > 0')
        except ValueError:
            self.label_3.setText('Введите число')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    my_app = MyWin()  # Создаём объект класса
    my_app.show()  # Показываем окно
    sys.exit(app.exec_())  # запускаем приложение
