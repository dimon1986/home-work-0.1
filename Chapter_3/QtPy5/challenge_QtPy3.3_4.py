import sys
import random
from M_Dawson_Home_Work.Chapter_3.QtPy5.challenge_QtPy3_3_4_Ui import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowTitle('Поиграй со мной')
        self.setWindowIcon(QIcon('data/doom/d'))
        # слова для проверки, что ввёл пользователь
        self.words = ['верно', 'больше', 'меньше']
        ####################################
        self.run = False  # запущина игра или нет
        self.run_two = False
        self.attempt = 0  # колличество попыток или шагов
        self.low = 0  # нижний придел
        self.high = 0  # верхний придел
        self.rand_digit = None  # рондомное значение
        self.answer = None  # наш отевет и цыфра и слово

        @self.pushButton_0.clicked.connect
        def click():
            self.run_game()  # вначале запускаем, потом меняем флаги и печатаем текст
            self.run = True
            self.run_two = False
            self.textEdit_1.setPlainText('')
            self.textEdit_0.setPlainText(f'Я загадал число от {self.low} до {self.high}, '
                                         f'у тебя {self.attempt+5} попыток одгадать число.\n')

        @self.pushButton_2.clicked.connect
        def click():
            self.run_game()  # вначале запускаем, потом меняем флаги и печатаем текст
            self.run_two = True
            self.run = False
            self.textEdit_0.setPlainText('')
            self.textEdit_1.setPlainText(f'Загадай натуральное число от {self.low} до {self.high}. '
                                         f'А я попробую вскрыть твой мозг(фигурально конечно):) '
                                         f'Пиши: верно-если отгадал, и больше или меньше, если нет.\n'
                                         f'таксс... это цыфра {self.rand_digit}\n')
        # проверка на валидноссть инпута
        self.pushButton_1.clicked.connect(self.validation)
        self.pushButton_3.clicked.connect(self.validation)

    def death_check(self):
        """главная функция смерти"""
        msg = self.textEdit_0.toPlainText()  # забираем значение текста
        if self.attempt < 5:  # проверяем не потратили бы мы все попытки
            self.attempt += 1  # шаг прибавляем
            if self.answer == self.rand_digit:  # сначало проверку, на отгдал или нет
                self.textEdit_0.setPlainText(f'Хорошо, ты отсрочил свою смерть.'
                                             f'\nЭто действительно {self.rand_digit}'
                                             f'\nПопыток использованно {self.attempt}.'
                                             f'\nНо я вернусь сюда.')
            if self.answer < self.rand_digit:  # тут всё ясно поровеки больше или меньше, наш ответ
                self.textEdit_0.setPlainText(f'{msg}\nТы ошибся значение больше!!'
                                             f'\nпопытка номер {self.attempt} закончилась.')
            if self.answer > self.rand_digit:
                self.textEdit_0.setPlainText(f'{msg}\nСмертный значение мешьше.'
                                             f'\nпопытка номер {self.attempt} закончилась.')
        else:
            add = '' # я тут понял PySide2 круче, так как пишет в чем ошибка:)
            if self.answer == self.rand_digit:
                add = 'Всё верно, но уже слишком позно.'
            self.textEdit_0.setPlainText(f'Ты был хорошим человеком, но это конец. '
                                         f'{add}'
                                         f'\nЧисло было: {self.rand_digit}')
            self.run = False
            self.statusbar.showMessage('Ты проиграл, можешь начать заново.')

    def mind_check(self):
        """функция проверки мозга, основные расчёты"""
        self.attempt += 1  # шаг прибавляем
        number = self.high - self.low  # от максимума отнимаем минимум, что бы было > 0
        if self.answer == 'верно':
            self.run_two = False  # останавливаем игру и вписываем поздравления
            self.textEdit_1.setPlainText('Ура РС отгадал!!Я взломал твой мозг. '
                                         f'Всего за {self.attempt} шагов.')
            if self.attempt > 5:  # шаги, есби больше 5 прибавляем надпись
                msg = self.textEdit_1.toPlainText()
                self.textEdit_1.setPlainText(f'{msg} Похоже я такойже быстрый как и i386...')
        else:
            msg = self.textEdit_1.toPlainText()
            if number > 0:  # если проверка успешна, то делаем модификации с мин и мах и рандит
                if self.answer == 'больше':
                    self.low = self.rand_digit + 1  # поднимаем нижнию границу, что бы разброс был меньше
                if self.answer == 'меньше':
                    self.high = self.rand_digit - 1  # уменьшаем верхнию границу, для того же
                # делаем рондом, по новой
                self.rand_digit = random.randint(self.low, self.high)
            # вписываем в сетПланТекст
            self.textEdit_1.setPlainText(f'{msg}таксс... это цыфра {self.rand_digit}\n')

    def validation(self):
        """функция проверки корректности ввода"""
        self.statusbar.showMessage("")  # по любому очищаем статус бар
        if self.run:  # если активна первая игра
            try:
                # превращаем в инт ответ
                self.answer = int(self.lineEdit_0.text())
            except ValueError:
                self.statusbar.showMessage('Ошибка ввода')
            else:
                # если ввод верный функция запускается
                # тут это не мешает, но всё же!
                self.death_check()
        #########################
        if self.run_two:  # если активна вторая игра
            try:
                # получаем ответ и проверка на вхождение, если что возбуждаем исключение
                self.answer = (self.lineEdit_1.text())
                if self.answer not in self.words:
                    raise ValueError
                # else: неполная форма исключения лучше работает - факт
                self.mind_check()
            except ValueError:
                self.statusbar.showMessage('Ошибка ввода')

    def run_game(self):
        # начальная функция, для запуска
        self.low = 0  # нижний придел - можно передать другие значения
        self.high = 100  # верхний придел
        self.statusbar.showMessage("")
        self.attempt = 0  # попытка
        # начальное значение рондома
        self.rand_digit = random.randint(self.low, self.high)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    my_app = MyWin()  # Создаём объект класса
    my_app.show()  # Показываем окно
    sys.exit(app.exec_())  # запускаем приложение
