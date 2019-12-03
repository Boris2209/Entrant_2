class Entrant:

    def __init__(self, surname, name, patronymic, date, passport,
                 diploma, gold_diploma, gold_gto, russian_exam, math_exam, informatics_exam,
                 check_diploma, check_consent, check_hostel):

        self.surname = surname          # фамилия
        self.name = name                # имя
        self.patronymic = patronymic    # отчество
        self.date = date                # дата рождения
        self.passport = passport        # даннеы пасспорта
        self.diploma = diploma          # данные аттестата
        self.gold_diploma = gold_diploma# аттестат с отличием
        self.gold_gto = gold_gto        # гто
        self.russian_exam = russian_exam
        self.math_exam = math_exam
        self.informatics_exam = informatics_exam
        self.check_diploma = check_diploma
        self.check_consent = check_consent
        self.check_hostel = check_hostel


    # возвращает ФИО
    def getFio(self):
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."

    # возвращает наличие золотой медали
    def getGoldDiploma(self):
        if self.gold_diploma:
            return True
        return False

    # возвращает наличие ГТО
    def getGoldGto(self):
        if self.gold_gto:
            return True
        return False

    # возвращает сумму баллов за экзамены
    def getSumExam(self):
        return int(self.russian_exam) + int(self.math_exam) + int(self.informatics_exam)

    # подлинник аттестата
    def getDiploma(self):
        if self.check_diploma:
            return True
        return False

    # согласие на зачисление
    def getConsest(self):
        if self.check_consent:
            return True
        return False




