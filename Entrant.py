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


    def getSurname(self):
        return self.surname

    def getName(self):
        return self.name

    def getPatronymic(self):
        return self.patronymic

    def getDate(self):
        return self.date

    def getPassport(self):
        return self.passport

    def getDiplom(self):
        return self.diploma




