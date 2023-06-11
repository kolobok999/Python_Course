# №7.1[###]. Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич
# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович
# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием
# os.path и pathlib
# MAIN_DIR = abspath(dirname(__file__))

from os.path import join, abspath, relpath, dirname, exists

MAIN_DIR = abspath(dirname(__file__))
filename = join(MAIN_DIR, "data", "data1.txt")
lst = list()
with open(filename, mode = "rt", encoding='utf-8') as file:
    for line in file:
        text = line.strip().split('#')
        # print(" ".join(text))
        lst.append(text)
print(lst)

# №7.2[###]. Продолжение предыдущей задачи
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# необходимо преобразовать к виду:
# Иванов И.И.
# Петров П.П.
# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
# В первый - в виде Иванов И.И.
# Во второй - в виде Иванов-И-И
# [*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много. Не две, а пять или десять
# Как улучшить свой код в этом случае, сделать его легко расширяемым?
def file_writer(file_name, specific):
    new_file = join(MAIN_DIR, "results", file_name)
    with open(new_file, mode = 'wt', encoding='utf-8') as file:
        for last_name, first_name, parent in lst:
            file.writelines(f"{last_name}{specific[0]}{first_name[0]}{specific[1]}{parent[0]}{specific[2]}\n")

file_writer('data2.txt', ' ..')
file_writer('data3.txt', '-- ')

# №7.3[###]. Имея список вида [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# преобразовать его в списки вида
# 1) ['Иванов-И-И', 'Петров-П-П', 'Соколов-И-Г'...]
# 2) ['Иванов И.И.', 'Петров П.П.', 'Соколов И.Г.'...]
# с использованием Comprehension; Comprehension + функция; Comprehension + lambda; map
# [**] Усложнение. Дополнить обработку списка условием: Выбираем только те элементы, в которых первая буква П

# Comprehension
lst2 = [f"{last_name}-{first_name[0]}-{parent[0]}" for last_name, first_name, parent in lst]
print(f'Comprehension: {lst2}')

# Comprehension + функция
def func1(lst1):
    return [f"{last_name} {first_name[0]}.{parent[0]}." for last_name, first_name, parent in lst1]
print(f'Comprehension + функция: {func1(lst)}')

# Comprehension + lambda
func2 = lambda obj : [f"{last_name} {first_name[0]}.{parent[0]}." for last_name, first_name, parent in obj]
print(f'Comprehension + lambda: {func2(lst)}')

# map
print(f'map: {list(map(lambda obj : f"{obj[0]} {obj[1][0]}.{obj[2][0]}.", lst))}')

# map [**]
print(f'map [**]: {list(map(lambda obj : f"{obj[0]} {obj[1][0]}.{obj[2][0]}.", filter(lambda x: x[0][0] == "П", lst)))}')