import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from graph import *
from PySide2 import QtCore, QtGui, QtWidgets
from Entrant import *



def append_entrant():
    e = Entrant(ui.line_surname.text(), ui.line_name.text(), ui.line_patronymic.text(),
                ui.date_of_birth.date(), ui.line_passport.text(), ui.line_diplom.text())






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # нажатие кнопки Добавить
    ui.button_append.clicked.connect(append_entrant)

    MainWindow.show()
    sys.exit(app.exec_())





