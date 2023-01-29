# Импортируем заранее написаные функции
from funcs import get_student_by_pk, get_profession_by_title, check_fitness

# Запрашиваем номер студента
pk = int(input('Введите номер студента'))

# Ищем студента по номеру в словаре, если студента нет выводим сообщение и заврешаем программу
student = get_student_by_pk(pk)
if student is None:
    print('У нас нет такого студента')
    quit()
print(f'Студент {student["full_name"]}\nЗнает {" ".join(student["skills"])}\n')

# Запрашиваем название профессии
title = input(f'Выберите специальность для оценки студента {student["full_name"]}\n').lower()

# Ищем профессию в словаре, если профессии нет выводим сообщение и заврешаем программу
profession = get_profession_by_title(title)
if profession is None:
    print('У нас нет такой специальности')
    quit()

# Проверяем пригодность студента и выводим ответ на экран
fitness = check_fitness(student, profession)

print(
    f'Пригодность {fitness["fit_percent"]}%\n{student["full_name"]} знает {" ".join(fitness["has"])}'
    f'\n{student["full_name"]} не знает {" ".join(fitness["lacks"])}')
