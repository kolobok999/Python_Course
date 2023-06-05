# №5.2[33]. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите функцию, которая заменяет оценки, переданные в виде списка, но наоборот: все максимальные – на минимальные.
# Функция должна возвращать новый список оценок
# Примечание: Обратите внимание на side effects функции.
# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]
# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None
# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.
# Примеры/Тесты:
# grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "enemy") -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

def change_grades(grades, loyalty = "enemy"):
    new_grades = grades.copy()
    min_grade = min(grades)
    max_grade = max(grades)
    if min_grade == max_grade:
        return None
    for idx, el in enumerate(grades):
        if el == max_grade and loyalty == "enemy":
            new_grades[idx] = min_grade
        if el == min_grade and loyalty == "friend":
            new_grades[idx] = max_grade
    return new_grades


grades_list = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# grades_list = [3, 3, 3, 3, 3, 3, 3, 3, 3]
print(change_grades(grades_list))
print(change_grades(grades_list, "friend"))
print(change_grades(grades_list, "enemy"))