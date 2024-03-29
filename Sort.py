import random


def sort_abc(list):
    """Сортирует абитуриентов по алфавиту, применяя алгоритм QuickSort"""
    if len(list) <= 1:
        return list
    else:
        q = random.choice(list)
        L = []
        M = []
        R = []
        for elem in list:
            if elem.getFio() < q.getFio():
                L.append(elem)
            elif elem.getFio() > q.getFio():
                R.append(elem)
            else:
                M.append(elem)
        return sort_abc(L) + M + sort_abc(R)


def sort_exam(list):
    """Сортирует абитуриентов по баллам, применяя алгоритм QuickSort"""
    if len(list) <= 1:
        return list
    else:
        q = random.choice(list)
        L = []
        M = []
        R = []
        for elem in list:
            if elem.getSumExam() > q.getSumExam():
                L.append(elem)
            elif elem.getSumExam() < q.getSumExam():
                R.append(elem)
            else:
                M.append(elem)
        return sort_exam(L) + M + sort_exam(R)