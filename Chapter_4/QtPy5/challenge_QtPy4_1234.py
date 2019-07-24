import sys
import random
from M_Dawson_Home_Work.Chapter_4.QtPy5.challenge_QtPy4_1234_Ui import *
from PyQt5 import QtWidgets, QtGui


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowTitle('Главный вопрос')
        self.setWindowIcon(QtGui.QIcon('data/q'))
        self.pushButton_0.clicked.connect(self.deem_run)
        self.lineEdit_3.textChanged.connect(self.mirror_txt)
        # отключаем кнопи проверки по умолчанию
        self.pushButton_2.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        # догадка пользователя
        self.guess = None

        self.pushButton_1.clicked.connect(self.click)
        self.pushButton_2.clicked.connect(self.check_guess)

        self.pushButton_3.clicked.connect(self.click)
        self.pushButton_4.clicked.connect(self.check_guess_two)

    def click(self):
        """Запуск той или иной игры"""
        def load_word():
            """метод загрузки слова """
            # загрузим последовательность слов делаем выбор
            with open('data/WORDS.txt', 'r', encoding='utf-8') as f:
                file = f.read()
                WORDS = file.split()
                # случайным образом выберем из последовательности одно слов
                word = random.choice(WORDS)
                return word
        # создадим переменную с которой будет затем сопоставлена версия игрока
        self.correct = load_word()
        # просто звёздочки по длине слова
        self.long = len(self.correct) * '*'
        # очки изначальные
        self.tip = 15

        sender = self.sender()
        if sender == self.pushButton_1:
            self.pushButton_2.setEnabled(True)
            self.pushButton_4.setEnabled(False)
            self.run_game()
        else:
            self.pushButton_4.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.run_game_two()

    def run_game_two(self):
        """просто приветствие, но можно добавить ещё чё нить"""
        self.textEdit_2.setPlainText(f'Добро пожаловать в игру Отгадай Слово!!\n'
                                     f'Если нужна помощь так и пишите.\n'
                                     f'Вот длинна слова: {len(self.correct)}\n')

    def check_guess_two(self):
        # просто проверка ответа и соответственное ветвление
        self.guess = self.lineEdit_6.text().lower()
        msg = self.textEdit_2.toPlainText()  # забираем значение текста
        # для каждого символа входящих в корект если да, то изменяем лонг, что бы звезды стали буквами
        if self.guess in self.correct:
            new = ''
            for i in range(len(self.correct)):
                if self.guess == self.correct[i]:
                    new += self.guess
                else:
                    new += self.long[i]
            self.long = new
            self.textEdit_2.setPlainText(f'{msg}\nВходит в состав слова.'
                                         f'\nЗагаданное слово сейчас выглядит так: {self.long}')
        # если ответ равен коретку или лонг корректу то конец и поздравления
        if self.guess == self.correct or self.long == self.correct:
            self.textEdit_2.setPlainText(f'Да, именно так! Вы отгадали!\n'
                                         f'Слово было: {self.correct.upper()}\n'
                                         f'Вы набрали {self.tip} очков - можете потратить их на поёздку на море.\n'
                                         f'Спасибо за игру.')
            self.pushButton_2.setEnabled(False)
        elif self.guess == 'помощь':  # всё как обычно помощь
            self.help_w(msg)
        elif self.guess not in self.correct:  # если не входит
            self.textEdit_2.setPlainText(f'{msg}\nК сожалению, вы не правы.\n')

    def run_game(self):
        """функция перемешивает слово и приветствует нас"""
        def create_jumble_word(word):
            # перемешивание слова
            jumble_word = ''
            while word:
                position = random.randrange(len(word))
                jumble_word += word[position]
                # создаём новое слово, делая срез удалением одной буквы, которую определил рондом
                word = word[:position] + word[(position + 1):]
            return jumble_word
        # создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
        self.jumble = create_jumble_word(self.correct)
        # просто выводим текст в текстэдит_1
        self.textEdit_1.setPlainText(f'Добро пожаловать в игру Анаграммы!!\n'
                                     f'Надо переставить буквы так, чтобы получилось осмысленое слово.\n'
                                     f'Если нужна помощь так и пишите.\n'
                                     f'Вот анаграмма: {self.jumble}\n')

    def help_w(self, msg, txt_one=None):
        # отнимаем очки, если взяли подсказку
        # всего 2раза отнимаем, что бы 5 осталось:)
        # ветвление по текстэдитам 1 и 2
        if self.tip == 15:
            txt_0 = f'{msg}\nВзял подсказку.\nПевая буква слова:' \
                    f'{self.correct[0]}{self.long[1:]}\n'
            if txt_one:
                self.textEdit_1.setPlainText(txt_0)
            else:
                self.textEdit_2.setPlainText(txt_0)
            self.tip -= 5
        elif self.tip == 10:
            txt_1 = f'{msg}\nВзял подсказку.\nПоследняя буква слова:' \
                    f'{self.correct[0]}{self.long[2:]}{self.correct[-1:]}\n'
            if txt_one:
                self.textEdit_1.setPlainText(txt_1)
            else:
                self.textEdit_2.setPlainText(txt_1)
            self.tip -= 5
        else:
            txt_2 = f'{msg}\nТы израсходовал все подсказки, что тебе ещё надо?'
            if txt_one:
                self.textEdit_1.setPlainText(txt_2)
            else:
                self.textEdit_2.setPlainText(txt_2)

    def check_guess(self):
        """записываем ответ, проверяем на корректность, если да то поздравляем и кнопку отключаем
        если помощь то вызываем помощь иначе говорим что нет таких"""
        self.guess = self.lineEdit_5.text().lower()
        msg = self.textEdit_1.toPlainText()  # забираем значение текста
        if self.guess == self.correct:
            self.textEdit_1.setPlainText(f'Да, именно так! Вы отгадали!\n'
                                         f'Вы набрали {self.tip} очков - можете потратить их на поёздку на море.\n'
                                         f'Спасибо за игру.')
            self.pushButton_2.setEnabled(False)
        if self.guess == 'помощь':
            self.help_w(msg, 1)
        elif self.guess != self.correct:
            self.textEdit_1.setPlainText(f'{msg}\nК сожалению, вы не правы.')

    def mirror_txt(self):
        """отражение текста однойстроки в другую"""
        reflection = self.lineEdit_3.text()
        new_msg = ''
        for letter in reflection[::-1]:
            new_msg += letter
        self.lineEdit_4.setText(new_msg)

    def deem_run(self, step=1, ):
        """по сути просто range только с интерактивностью"""
        try:
            start = int(self.lineEdit_0.text())
            end = int((self.lineEdit_1.text()))
            try: # если степ введён, то его читаем, инече по умолчанию
                step = int((self.lineEdit_2.text()))
            except ValueError:
                step = step
            # если конец меньше начала, то шаг делаем отрицательный
            if end < start:
                step = - step
            # порядок всех чисел - генерируем список
            order = [i for i in range(start, end, step)]
            # вносим его в тексэдит_0
            self.textEdit_0.setPlainText(f'{order}\nВот список значений.')
            # если не то ввели
        except ValueError:
            self.statusbar.showMessage('Введи целочисленное значение!', 2000)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())
