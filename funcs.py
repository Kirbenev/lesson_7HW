import json

 #Создаем необходимые функции

def load_students(filename):

    """ Функция загружает список студентов из JSON Файла """

    with open(filename) as f:
        raw_json = f.read()
    return json.loads(raw_json)


def load_professions(filename):
    """ Функция загружает список профессий из JSON Файла """
    with open(filename) as f:
        raw_json = f.read()
    return json.loads(raw_json)


def get_student_by_pk(pk):
    """ Функция ищет студента по номеру и возращает его данные"""
    for item in load_students("students.json"):
        if item["pk"] == pk:
            student = {"full_name": item["full_name"], "skills": item["skills"]}
            return student
    return None


def get_profession_by_title(title):
    """ Функция ищет профессию в списке и возвращает словарь с названием и требованиями к профессии """
    for item in load_professions("professions.json"):
        if item["title"].lower() == title:
            profession = {"title": item["title"].lower(), "skills": item["skills"]}
            return profession
    return None


def check_fitness(student, profession):
    """ Функция проверяет подходит ли студент под выбранную профессию и возваращает словарь с навыками и процент соответсвия студента профессии  """
    student_lang = set(student["skills"])
    prof_lang = set(profession["skills"])
    has = list(student_lang.intersection(prof_lang))
    lacks = list(prof_lang.difference(student_lang))
    fit_percent = int(len(has) / len(prof_lang) * 100)
    fitness = {
        "has": has,
        "lacks": lacks,
        "fit_percent": fit_percent
    }
    return fitness
