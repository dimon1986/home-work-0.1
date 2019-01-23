import sys

from M_Dawson_Home_Work.Chapter_2.QtPy5.challenge_QtPy2_3_Ui import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class MyWin(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowTitle('Автодиллир')
        self.setWindowIcon(QIcon('data/cars/light'))
        self.horizontalSlider_0.valueChanged[int].connect(self.price_car)

        @self.horizontalSlider_1.valueChanged.connect
        def click(value):
            self.tax(value)

        @self.horizontalSlider_2.valueChanged.connect
        def click(value):
            # передаём параметор ту, что бы знать, какой слайдер задействовали
            self.tax(value, tu='Slider_2')

        self.horizontalSlider_3.valueChanged[int].connect(self.agency_fee)
        self.horizontalSlider_4.valueChanged[int].connect(self.delivery)
        # будут значения агенского сбора и доставки храниться
        # значения по дефолту
        self.dict_digit = {'agency_fee': 1000, 'delivery': 5000 }

    def price_car(self, value, ):
        """не знаю насколько это красивно,но удобно"""
        self.label_0.setText(f'Цена : {value}')
        self.tax(self.horizontalSlider_1.value())
        self.tax(self.horizontalSlider_2.value(), tu='Slider_2')
        self.sum_tax()
        # проверка какую картинку поставить
        if value <= 25000:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/light'))
        elif value <= 50000:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/lada'))
        elif value <= 100000:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/niva'))
        elif value <= 150000:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/scooter'))
        elif value <= 250000:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/skoda'))
        elif value <= 450000:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/toyota.png'))
        elif value <= 650000:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/mercedes'))
        elif value <= 850000:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/cadillac'))
        elif value <= 50000:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/porsche'))
        else:
            self.label_img.setPixmap(QtGui.QPixmap('data/cars/rolls_royce'))

    def tax(self, value, tu=None):
        """единая функция, хоть и не очень красивая"""
        worth = self.horizontalSlider_0.value()
        worth *= (value/100)  # получаем допустим 0.5 и умножаем на цену value
        if not tu:
            self.label_1.setText(f'Налог : {int(worth)}')
        else:
            self.label_2.setText(f'Регистрационный сбор : {int(worth)}')
        # не забываем, что мы последовательны
        # пересчёт всех такс
        self.sum_tax()

    def agency_fee(self, value):
        """функция просто меняет занчения у словаря"""
        def fee_print(fee):
            """для уменьшения кода и добавления текста лейбла"""
            self.dict_digit['agency_fee'] = fee
            self.label_3.setText(f'Агентский сбор : {fee}')
        if value == 0:
            fee = 1000
        elif value == 1:
            fee = 2000
        elif value == 2:
            fee = 4000
        elif value == 3:
            fee = 8000
        elif value == 4:
            fee = 16000
        else:
            fee = 32000
        fee_print(fee)
        # не забываем, что мы последовательны
        # пересчёт всех такс
        self.sum_tax()

    def delivery(self, value):
        """оставлю для примера как раньше делал,
        может даже так удобнее читать"""
        if value == 0:
            self.label_4.setText('Доставка эконом : 1000')
            self.dict_digit['delivery'] = 1000
        elif value == 1:
            self.label_4.setText('Доставка обычная : 5000')
            self.dict_digit['delivery'] = 5000
        else:
            self.label_4.setText('Доставка элита : 7500')
            self.dict_digit['delivery'] = 7500
        # пересчёт всех такс
        self.sum_tax()

    def sum_tax(self):
        """просто окончательный пересчёт
        итого общее"""
        price_car = self.horizontalSlider_0.value()
        tax = price_car * (self.horizontalSlider_1.value()/100)
        registration_fee = price_car * (self.horizontalSlider_2.value()/100)
        agency_delivery = 0
        for j in self.dict_digit.values():
            agency_delivery += j
        self.label_q_1.setText(f'Итого: '
                               f'{agency_delivery + price_car + int(tax) + int(registration_fee)}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    my_app = MyWin()  # Создаём объект класса
    my_app.show()  # Показываем окно
    sys.exit(app.exec_())  # запускаем приложение
