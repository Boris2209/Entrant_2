class Entrant:

    def __init__(self, surname, name, patronymic, date, passport,
                 diploma, gold_diploma, gold_gto, russian_exam, math_exam, informatics_exam,
                 check_diploma, check_consent, check_hostel):

        self.surname = surname                          # фамилия
        self.name = name                                # имя
        self.patronymic = patronymic                    # отчество
        self.date = date                                # дата рождения
        self.passport = passport                        # даннеы пасспорта
        self.diploma = diploma                          # данные аттестата
        self.gold_diploma = gold_diploma                # аттестат с отличием
        self.gold_gto = gold_gto                        # гто
        self.russian_exam = russian_exam                # баллы за русский
        self.math_exam = math_exam                      # баллы за математиу
        self.informatics_exam = informatics_exam        # баллы за информатику
        self.check_diploma = check_diploma              # наличие подлинника
        self.check_consent = check_consent              # наличие согласия на зачисление
        self.check_hostel = check_hostel                # требуется ли общежитие

    # возвращает ФИО
    def getFio(self):
        if self.patronymic[0] is "-":
            return self.surname + " " + self.name[0] + "."
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."

    # возвращает сумму баллов за экзамены
    def getSumExam(self):
        return int(self.russian_exam) + int(self.math_exam) + int(self.informatics_exam)





