# №6.3[43] Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.
# Напишите функцию
# Аргументы: список целых чисел
# Возвращает: кол-во пар
# Примеры/Тесты:
# <function_name>([1, 2, 3, 2, 3]) -> 2
# <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6

def same_pair(lst: list) -> int:
    sum = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                sum += 1
    return sum

def same_pair2(lst: list) -> int:
    sum = 0
    for idx in range(len(lst) - 1):
        sum += lst[idx + 1:].count(lst[idx])
    return sum

print(same_pair([1, 2, 3, 2, 3]))
print(same_pair([1, 2, 3, 2, 3, 3, 2, 4]))

print(same_pair2([1, 2, 3, 2, 3]))
print(same_pair2([1, 2, 3, 2, 3, 3, 2, 4]))