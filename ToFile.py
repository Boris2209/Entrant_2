from Huffman import *
from PySide2.QtWidgets import QMessageBox
import pickle
from Entrant import *


def encode_to_file(list_entrant, url):
    # необходимо список абитуриентов преобраховать к строке
    # символ | будет разделять поля, а символ \n абитуриентов
    str_entrant = ""
    for entrant in list_entrant:
        str_entrant += (entrant.surname + "|")
        str_entrant += (entrant.name + "|")
        str_entrant += (entrant.patronymic + "|")

        str_entrant += (str(entrant.date) + "|")
        str_entrant += (entrant.passport + "|")
        str_entrant += (entrant.diploma + "|")

        if entrant.gold_diploma:
            str_entrant += "1|"
        else:
            str_entrant += "0|"

        if entrant.gold_gto:
            str_entrant += "1|"
        else:
            str_entrant += "0|"

        str_entrant += (entrant.russian_exam + "|")
        str_entrant += (entrant.math_exam + "|")
        str_entrant += (entrant.informatics_exam + "|")

        if entrant.check_diploma:
            str_entrant += "1|"
        else:
            str_entrant += "0|"

        if entrant.check_consent:
            str_entrant += "1|"
        else:
            str_entrant += "0|"

        if entrant.check_hostel:
            str_entrant += "1*"
        else:
            str_entrant += "0*"

    code = huffman_encode(str_entrant)  # получаем словарь символ  :код
    str_code = "".join(code[ch] for ch in str_entrant)  # закодированная строка

    try:
        # файл с кодом
        fil = open('test.txt', 'wt')
        fil.write(str_code)
        fil.close()

        # файл с ключом (словарем символов)
        with open('data.pickle', 'wb') as f:
            pickle.dump(code, f)

        mes = QMessageBox()
        mes.setText("Запись прошла успешно!")
        mes.setWindowTitle("Поздравляем")
        mes.exec_()
    except Exception:
        mess = QMessageBox()
        mess.setText("Ошибка записи!")
        mess.setWindowTitle("Ошибка")
        mess.exec_()


def decode_to_file(url):
    #try:
        # полчуим ключ (словарь исмволов)
        with open('data.pickle', 'rb') as f:
            code = pickle.load(f)

        print(code)

        # полчуим закодированную строку
        fil = open('test.txt', 'rb')
        str_code = fil.read().decode("utf-8")
        fil.close()

        str_code = str_code[0:-1]
        print(str_code)

        str_entrant = huffman_decode(str_code, code)    # раскодируем строку

        print(str_entrant)

        list_entrant = []   # список абитуриентов

        str_entrant_list = []
        str_entrant_list = str_entrant.split("*")  # делим строку по абитуриенту



        print(str_entrant_list)

        # циклом разбираем
        for entrant in str_entrant_list:

            entrant_list = []
            entrant_list = entrant.split("|")
            print(entrant_list)
            list_entrant.append(Entrant(entrant_list[0], entrant_list[1], entrant_list[2], entrant_list[3],
                                        entrant_list[4], entrant_list[5], entrant_list[6], entrant_list[7],
                                        entrant_list[8], entrant_list[9], entrant_list[10], entrant_list[11],
                                        entrant_list[12], entrant_list[13]))

        return list_entrant
    #xcept Exception:
       # mess = QMessageBox()
       #mess.setText("Ошибка чтения!")
        #mess.setWindowTitle("Ошибка")
        #mess.exec_()
