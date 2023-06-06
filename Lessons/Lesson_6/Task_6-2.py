# №6.2[41] Дан список, целых чисел.
# Напишите функцию, которая определит те элементы списка, у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Функция
# Аргументы: список целых чисел
# Возвращает: список элементов (смотри условие)
# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 5]) -> [5]
# <function_name>([1, 5, 1, 6, 1]) -> [5,6]
# <function_name>([7, 5, 1, 6, 8]) -> [8]
# <function_name>([8, 1, 5, 4, 5]) -> [8,5]

def func(lst:list)-> list:
    new_lst = []
    for idx, el in enumerate(lst):
        if el > lst[idx -1] and el > lst[idx - len(lst) + 1]:
            new_lst.append(el)
    return new_lst

print(func([1, 3, 3, 3, 5]))
print(func([1, 5, 1, 6, 1]))
print(func([7, 5, 1, 6, 8]))
print(func([8, 1, 5, 4, 5]))