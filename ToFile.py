from Huffman import *
from PySide2.QtWidgets import QMessageBox
import pickle


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
            str_entrant += "1\n"
        else:
            str_entrant += "0\n"

    code = huffman_encode(str_entrant)  # получаем словарь символ  :код
    str_code = "".join(code[ch] for ch in str_entrant)  # закодированная строка

    try:
        # файл с кодом
        fil = open('text.txt', 'wt')
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

