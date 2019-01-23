import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel,
                             QLineEdit, QPushButton, QComboBox, QInputDialog)
from PyQt5.QtGui import QIcon, QFont, QPixmap


class Challenge(QWidget):

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(1)

        self.lbl0 = QLabel('"В начале было Слово"', self)  # создал лейбол
        self.lbl0.setFont(QFont('Times New Roman', 18))
        grid.addWidget(self.lbl0, 0, 0)  # добавил в виджет

        self.lbl1 = QLabel('"и Слово было"', self)  # создал лейбол
        self.lbl1.setFont(QFont('Times New Roman', 14))
        grid.addWidget(self.lbl1, 1, 0)  # добавил в виджет

        self.lbl2 = QLabel('"?"', self)  # создал лейбол
        self.lbl2.setFont(QFont('Times New Roman', 12))
        grid.addWidget(self.lbl2, 2, 0,)  # добавил в виджет

        qle = QLineEdit(self)
        grid.addWidget(qle, 3, 0)
        qle.textChanged[str].connect(self.on_changed)

        qbtn = QPushButton('Цитата', self)
        qbtn.setToolTip('Add quote <b>QPushButton</b> widget')
        qbtn.clicked.connect(self.show_dialog)
        grid.addWidget(qbtn, 0,1)

        self.lbl3 = QLabel('Выбери мороженное', self)  # создал лейбол
        grid.addWidget(self.lbl3, 1, 1)  # добавил в виджет
        self.combo = QComboBox(self)
        self.combo.addItems(["Клубничное", "Вишнёвое",
                             "Шоколадное", "Черничное"])
        self.combo.activated[str].connect(self.on_activated)
        grid.addWidget(self.combo, 2, 1)

        self.icecream = QLabel(self)
        self.icecream.setPixmap(QPixmap('data/ice_s'))
        grid.addWidget(self.icecream, 3, 1, )

        self.setGeometry(300, 300, 480, 320)
        self.setWindowTitle('Ice cream & co')
        self.setWindowIcon(QIcon('data/ice'))
        self.show()

    def on_changed(self, text):
        """просто вписывае текст в лейбл"""
        self.lbl2.setText(f'"{text}"')

    def on_activated(self, text):
        """перекючение картинки, взависимости от текста комбобокса"""
        if text == "Клубничное":
            self.icecream.setPixmap(QPixmap('data/ice_s'))
        elif text == "Вишнёвое":
            self.icecream.setPixmap(QPixmap('data/ice_ch'))
        elif text == "Шоколадное":
            self.icecream.setPixmap(QPixmap('data/ice_c'))
        else:
            self.icecream.setPixmap(QPixmap('data/ice_b'))

    def show_dialog(self):
        """простой диалог"""
        text, ok = QInputDialog.getText(self, 'Диалог', 'Добавьте цитату:')
        # текст - это то что вводим в диалоге, а ок может быть любой переменной
        if ok:
            self.lbl1.setText(str(f'"{text}"'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cl = Challenge()
    sys.exit(app.exec_())