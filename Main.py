import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import QMessageBox

from graph import *
from PySide2 import QtCore, QtGui, QtWidgets
from Entrant import *
from Sort import *
from ToFile import *


# хрнаим в списке список всех абитуриентов
list_entrant = []


def clear_lines():
    ui.line_surname.clear()
    ui.line_name.clear()
    ui.line_patronymic.clear()
    ui.date_of_birth.setDate(QDate.currentDate())
    ui.line_passport.clear()
    ui.line_diplom.clear()
    ui.check_gold_diplom.setChecked(False)
    ui.check_GTO.setChecked(False)
    ui.line_russian.clear()
    ui.line_math.clear()
    ui.line_informatics.clear()
    ui.check_diplom.setChecked(False)
    ui.check_consent.setChecked(False)
    ui.check_hostel.setChecked(False)


def append_entrant():
    """Считывает данные из полей, добавляет в список и очищает поля"""
    try:

        list_entrant.append(Entrant(ui.line_surname.text(), ui.line_name.text(), ui.line_patronymic.text(),
                    ui.date_of_birth.date(), ui.line_passport.text(), ui.line_diplom.text(),
                    ui.check_gold_diplom.checkState(), ui.check_GTO.checkState(), ui.line_russian.text(),
                    ui.line_math.text(), ui.line_informatics.text(), ui.check_diplom.checkState(),
                    ui.check_consent.checkState(), ui.check_hostel.checkState()))

        display_list(list_entrant)

        clear_lines()

    except Exception as e:
        mess = QMessageBox()
        mess.setText("Ошибка ввода!")
        mess.setWindowTitle("Ошибка")
        mess.exec_()
        print(e)


def getStringEntarnt(entrant):
    """Получает на вход абитуриента, выдает строку, нормализованную для вывода"""
    strE = ""   # в нее собирается информация

    # будем дописывать пробелы, что бы конечный список был ровным

    # ФИО
    fio = entrant.getFio()
    while len(fio) < 25:
        fio += " "
    strE += fio

    # сумма баллов за экзамен
    ball = str(entrant.getSumExam())
    while len(ball) < 10:
        ball += " "
    strE += ball

    # золтая медаль
    if entrant.gold_diploma:
        gold = "Да"
    else:
        gold = "Нет"
    while len(gold) < 10:
        gold += " "
    strE += gold

    # ГТО
    if entrant.gold_gto:
        gold = "Да"
    else:
        gold = "Нет"
    while len(gold) < 10:
        gold += " "
    strE += gold

    # подлинник
    if entrant.check_diploma:
        diploma = "Да"
    else:
        diploma = "Нет"
    while len(diploma) < 10:
        diploma += " "
    strE += diploma

    # согласие на зачисление
    if entrant.check_consent:
        consest = "Да"
    else:
        consest = "Нет"
    while len(consest) < 10:
        consest += " "
    strE += consest

    return (strE + "\n")


def display_list(list):
    """Напечатает на дисплей список, который в него предается"""
    strE = ("ФИО                      " + "Баллы     " + "Золото    " + "ГТО       " +
            "Подлинник " + "Согласие" + "\n\n")

    for e in list:
        strE += getStringEntarnt(e)

    ui.list_e.setText(strE)


def sort_list():
    # создадим новый список
    list_entrant_2 = []
    # если нужны только абитуриенты, допущеные к зачислению
    if ui.checkBox_entrant.checkState():
        for e in list_entrant:
            if e.check_diploma and e.check_consent:
                list_entrant_2.append(e)

    else:
        for e in list_entrant:
            list_entrant_2.append(e)

    # сортировка по алфавиту
    if ui.comboBox_sort.currentIndex() is 1:
        display_list(sort_abc(list_entrant_2))
    # сортировка по балалм
    elif ui.comboBox_sort.currentIndex() is 0:
        display_list(sort_exam(list_entrant_2))


def in_file():
    encode_to_file(list_entrant)


def out_file():
    global list_entrant
    list_entrant = decode_to_file()
    display_list(list_entrant)


def delete_list():
    list_entrant.clear()
    display_list(list_entrant)
    clear_lines()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # установим условие, что бы можно было ввести только числа 0-100 в поля результатов экзаменов
    ui.line_russian.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('(100)|(\d{1,2})')))
    ui.line_math.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('(100)|(\d{1,2})')))
    ui.line_informatics.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('(100)|(\d{1,2})')))

    # в лчиные данные только символы кириллицы, первая заглавная
    ui.line_surname.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('^[А-Я][а-я]+$')))
    ui.line_name.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('^[А-Я][а-я]+$')))
    ui.line_patronymic.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('(-)|(^[А-Я][а-я]+$)')))

    # а вместо даты рождени будет показываться текщая дата
    ui.date_of_birth.setDate(QDate.currentDate())

    # сразу будет показываться структура отображения
    display_list(list_entrant)

    # инициализация Combo Box (вариант сортировки)
    ui.comboBox_sort.addItem("Убыванию баллов")
    ui.comboBox_sort.addItem("Алфавиту")

    # нажатие кнопки Добавить
    ui.button_append.clicked.connect(append_entrant)

    # нажатие кнопки сортировать
    ui.pushButton_sort.clicked.connect(sort_list)

    # нажатие кнопки Загрузить в файл
    ui.button_file_in.clicked.connect(in_file)

    # нажатие кнопки Загрузить из файла
    ui.button_file_out.clicked.connect(out_file)

    # нажатие кнопки очистить список
    ui.button_delete.clicked.connect(delete_list)

    MainWindow.show()
    sys.exit(app.exec_())
