import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from graph import *
from PySide2 import QtCore, QtGui, QtWidgets
from Entrant import *


# хрнаим в списке список всех абитуриентов

def append_entrant():
    e = Entrant(ui.line_surname.text(), ui.line_name.text(), ui.line_patronymic.text(),
                ui.date_of_birth.date(), ui.line_passport.text(), ui.line_diplom.text(),
                ui.check_gold_diplom.checkState(), ui.check_GTO.checkState(), ui.line_russian.text(),
                ui.line_math.text(), ui.line_informatics.text(), ui.check_diplom.checkState(),
                ui.check_consent.checkState(), ui.check_hostel.checkState())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # установим условие, что бы можно было ввести только числа 0-100 в поля результатов экзаменов
    ui.line_russian.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('(100)|(0*\d{1,2})')))
    ui.line_math.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('(100)|(0*\d{1,2})')))
    ui.line_informatics.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('(100)|(0*\d{1,2})')))

    # в лчиные данные только символы кириллицы, первая заглавная
    ui.line_surname.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('^[А-Я][а-я]+$')))
    ui.line_name.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('^[А-Я][а-я]+$')))
    ui.line_patronymic.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('^[А-Я][а-я]+$')))


    # нажатие кнопки Добавить
    ui.button_append.clicked.connect(append_entrant)

    MainWindow.show()
    sys.exit(app.exec_())
