# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'challenge_QtPy1.12.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 848)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 836, 822))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_8 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 10, 0, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout.addWidget(self.checkBox_1, 3, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 9, 0, 1, 1)
        self.checkBox_0 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_0.setObjectName("checkBox_0")
        self.gridLayout.addWidget(self.checkBox_0, 2, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 8, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 7, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 6, 0, 1, 1)
        self.label_0 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.gridLayout.addWidget(self.label_0, 0, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 12, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 13, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 4, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkBox_9 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 11, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_waiter = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_waiter.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_waiter.setMouseTracking(False)
        self.label_waiter.setStatusTip("")
        self.label_waiter.setText("")
        self.label_waiter.setPixmap(QtGui.QPixmap("data/waiter_0.png"))
        self.label_waiter.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_waiter.setObjectName("label_waiter")
        self.verticalLayout.addWidget(self.label_waiter, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.radioButton_0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_0.setObjectName("radioButton_0")
        self.verticalLayout.addWidget(self.radioButton_0)
        self.radioButton_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_8.setText(_translate("MainWindow", "Коньяк"))
        self.checkBox_1.setText(_translate("MainWindow", "Майонез"))
        self.checkBox_7.setText(_translate("MainWindow", "Канапля"))
        self.checkBox_0.setText(_translate("MainWindow", "Макороны"))
        self.checkBox_6.setText(_translate("MainWindow", "Картошка"))
        self.checkBox_5.setText(_translate("MainWindow", "Водка"))
        self.checkBox_4.setText(_translate("MainWindow", "Мясо"))
        self.label_0.setText(_translate("MainWindow", "Выберите еду:"))
        self.checkBox_3.setText(_translate("MainWindow", "Молоко"))
        self.pushButton.setText(_translate("MainWindow", "Случайно"))
        self.checkBox_2.setText(_translate("MainWindow", "Мороженое"))
        self.label_1.setText(_translate("MainWindow", "стол для худеющих"))
        self.checkBox_9.setText(_translate("MainWindow", "Шоколад"))
        self.label_2.setText(_translate("MainWindow", "Каков ваш счёт?"))
        self.radioButton_0.setText(_translate("MainWindow", "0% чаявых"))
        self.radioButton_1.setText(_translate("MainWindow", "15% чаявых"))
        self.radioButton_2.setText(_translate("MainWindow", "20% чаявых"))
        self.label_3.setText(_translate("MainWindow", "Итого: "))

