# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui',
# licensing of 'graph.ui' applies.
#
# Created: Sat Dec  7 00:19:43 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1192, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_out_abitur = QtWidgets.QGroupBox(self.centralwidget)
        self.group_out_abitur.setEnabled(True)
        self.group_out_abitur.setGeometry(QtCore.QRect(10, 10, 351, 850))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.group_out_abitur.setFont(font)
        self.group_out_abitur.setTitle("")
        self.group_out_abitur.setObjectName("group_out_abitur")
        self.line_surname = QtWidgets.QLineEdit(self.group_out_abitur)
        self.line_surname.setGeometry(QtCore.QRect(10, 30, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_surname.setFont(font)
        self.line_surname.setObjectName("line_surname")
        self.line_name = QtWidgets.QLineEdit(self.group_out_abitur)
        self.line_name.setGeometry(QtCore.QRect(10, 80, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_name.setFont(font)
        self.line_name.setObjectName("line_name")
        self.line_patronymic = QtWidgets.QLineEdit(self.group_out_abitur)
        self.line_patronymic.setGeometry(QtCore.QRect(10, 130, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_patronymic.setFont(font)
        self.line_patronymic.setObjectName("line_patronymic")
        self.line_passport = QtWidgets.QLineEdit(self.group_out_abitur)
        self.line_passport.setGeometry(QtCore.QRect(10, 230, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_passport.setFont(font)
        self.line_passport.setObjectName("line_passport")
        self.label_surname = QtWidgets.QLabel(self.group_out_abitur)
        self.label_surname.setGeometry(QtCore.QRect(10, 10, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_surname.setFont(font)
        self.label_surname.setObjectName("label_surname")
        self.label_name = QtWidgets.QLabel(self.group_out_abitur)
        self.label_name.setGeometry(QtCore.QRect(10, 60, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_patronymic = QtWidgets.QLabel(self.group_out_abitur)
        self.label_patronymic.setGeometry(QtCore.QRect(10, 110, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_patronymic.setFont(font)
        self.label_patronymic.setObjectName("label_patronymic")
        self.label_passport = QtWidgets.QLabel(self.group_out_abitur)
        self.label_passport.setGeometry(QtCore.QRect(10, 210, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_passport.setFont(font)
        self.label_passport.setObjectName("label_passport")
        self.line_diplom = QtWidgets.QLineEdit(self.group_out_abitur)
        self.line_diplom.setGeometry(QtCore.QRect(10, 280, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_diplom.setFont(font)
        self.line_diplom.setObjectName("line_diplom")
        self.label_diplom = QtWidgets.QLabel(self.group_out_abitur)
        self.label_diplom.setGeometry(QtCore.QRect(10, 260, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_diplom.setFont(font)
        self.label_diplom.setObjectName("label_diplom")
        self.check_gold_diplom = QtWidgets.QCheckBox(self.group_out_abitur)
        self.check_gold_diplom.setGeometry(QtCore.QRect(10, 310, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_gold_diplom.setFont(font)
        self.check_gold_diplom.setObjectName("check_gold_diplom")
        self.check_GTO = QtWidgets.QCheckBox(self.group_out_abitur)
        self.check_GTO.setGeometry(QtCore.QRect(10, 340, 250, 20))
        self.check_GTO.setObjectName("check_GTO")
        self.check_hostel = QtWidgets.QCheckBox(self.group_out_abitur)
        self.check_hostel.setGeometry(QtCore.QRect(10, 630, 250, 20))
        self.check_hostel.setObjectName("check_hostel")
        self.check_diplom = QtWidgets.QCheckBox(self.group_out_abitur)
        self.check_diplom.setGeometry(QtCore.QRect(10, 530, 250, 20))
        self.check_diplom.setObjectName("check_diplom")
        self.check_consent = QtWidgets.QCheckBox(self.group_out_abitur)
        self.check_consent.setGeometry(QtCore.QRect(10, 560, 250, 20))
        self.check_consent.setObjectName("check_consent")
        self.date_of_birth = QtWidgets.QDateEdit(self.group_out_abitur)
        self.date_of_birth.setGeometry(QtCore.QRect(150, 170, 110, 22))
        self.date_of_birth.setObjectName("date_of_birth")
        self.label_birth = QtWidgets.QLabel(self.group_out_abitur)
        self.label_birth.setGeometry(QtCore.QRect(10, 170, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_birth.setFont(font)
        self.label_birth.setObjectName("label_birth")
        self.button_append = QtWidgets.QPushButton(self.group_out_abitur)
        self.button_append.setGeometry(QtCore.QRect(10, 780, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_append.setFont(font)
        self.button_append.setObjectName("button_append")
        self.label_result_exam = QtWidgets.QLabel(self.group_out_abitur)
        self.label_result_exam.setGeometry(QtCore.QRect(10, 390, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_result_exam.setFont(font)
        self.label_result_exam.setObjectName("label_result_exam")
        self.label_russian = QtWidgets.QLabel(self.group_out_abitur)
        self.label_russian.setGeometry(QtCore.QRect(10, 420, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_russian.setFont(font)
        self.label_russian.setObjectName("label_russian")
        self.label_math = QtWidgets.QLabel(self.group_out_abitur)
        self.label_math.setGeometry(QtCore.QRect(10, 450, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_math.setFont(font)
        self.label_math.setObjectName("label_math")
        self.label_inform = QtWidgets.QLabel(self.group_out_abitur)
        self.label_inform.setGeometry(QtCore.QRect(10, 480, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_inform.setFont(font)
        self.label_inform.setObjectName("label_inform")
        self.line_russian = QtWidgets.QLineEdit(self.group_out_abitur)
        self.line_russian.setGeometry(QtCore.QRect(110, 420, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_russian.setFont(font)
        self.line_russian.setObjectName("line_russian")
        self.line_math = QtWidgets.QLineEdit(self.group_out_abitur)
        self.line_math.setGeometry(QtCore.QRect(110, 450, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_math.setFont(font)
        self.line_math.setObjectName("line_math")
        self.line_informatics = QtWidgets.QLineEdit(self.group_out_abitur)
        self.line_informatics.setGeometry(QtCore.QRect(110, 480, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_informatics.setFont(font)
        self.line_informatics.setObjectName("line_informatics")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 10, 721, 850))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.list_e = QtWidgets.QTextEdit(self.groupBox_2)
        self.list_e.setGeometry(QtCore.QRect(10, 10, 701, 611))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.list_e.setFont(font)
        self.list_e.setReadOnly(True)
        self.list_e.setObjectName("list_e")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 640, 701, 201))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_sort = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sort.setEnabled(True)
        self.pushButton_sort.setGeometry(QtCore.QRect(554, 62, 121, 31))
        self.pushButton_sort.setObjectName("pushButton_sort")
        self.comboBox_sort = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_sort.setEnabled(True)
        self.comboBox_sort.setGeometry(QtCore.QRect(140, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_sort.setFont(font)
        self.comboBox_sort.setObjectName("comboBox_sort")
        self.checkBox_entrant = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_entrant.setEnabled(True)
        self.checkBox_entrant.setGeometry(QtCore.QRect(430, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_entrant.setFont(font)
        self.checkBox_entrant.setObjectName("checkBox_entrant")
        self.label_sort = QtWidgets.QLabel(self.groupBox)
        self.label_sort.setEnabled(True)
        self.label_sort.setGeometry(QtCore.QRect(10, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sort.setFont(font)
        self.label_sort.setObjectName("label_sort")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Учет абитуриентов ИИТ", None, -1))
        self.label_surname.setText(QtWidgets.QApplication.translate("MainWindow", "Фамилия", None, -1))
        self.label_name.setText(QtWidgets.QApplication.translate("MainWindow", "Имя", None, -1))
        self.label_patronymic.setText(QtWidgets.QApplication.translate("MainWindow", "Отчество", None, -1))
        self.label_passport.setText(QtWidgets.QApplication.translate("MainWindow", "Серия и номер паспорта", None, -1))
        self.label_diplom.setText(QtWidgets.QApplication.translate("MainWindow", "Серия и номер аттестата", None, -1))
        self.check_gold_diplom.setText(QtWidgets.QApplication.translate("MainWindow", "Аттестат с отличием", None, -1))
        self.check_GTO.setText(QtWidgets.QApplication.translate("MainWindow", "Золотой значок ГТО", None, -1))
        self.check_hostel.setText(QtWidgets.QApplication.translate("MainWindow", "Требуется общежитие", None, -1))
        self.check_diplom.setText(QtWidgets.QApplication.translate("MainWindow", "Подлинник аттестата", None, -1))
        self.check_consent.setText(QtWidgets.QApplication.translate("MainWindow", "Согласие на зачисление", None, -1))
        self.label_birth.setText(QtWidgets.QApplication.translate("MainWindow", "Дата рождения", None, -1))
        self.button_append.setText(QtWidgets.QApplication.translate("MainWindow", "Добавить", None, -1))
        self.label_result_exam.setText(QtWidgets.QApplication.translate("MainWindow", "Результаты экзаменов:", None, -1))
        self.label_russian.setText(QtWidgets.QApplication.translate("MainWindow", "Русский язык:", None, -1))
        self.label_math.setText(QtWidgets.QApplication.translate("MainWindow", "Математика:", None, -1))
        self.label_inform.setText(QtWidgets.QApplication.translate("MainWindow", "Информатика:", None, -1))
        self.pushButton_sort.setText(QtWidgets.QApplication.translate("MainWindow", "Сортировать", None, -1))
        self.checkBox_entrant.setText(QtWidgets.QApplication.translate("MainWindow", "Рассматривается к зачислению", None, -1))
        self.label_sort.setText(QtWidgets.QApplication.translate("MainWindow", "Сортировать по:", None, -1))

