class Entrant:

    def __init__(self, surname, name, patronymic, date, passport, diplom):

        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.date = date
        self.passport = passport
        self.diplom = diplom


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
        return self.diplom


