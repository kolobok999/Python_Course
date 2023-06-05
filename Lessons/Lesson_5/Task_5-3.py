# №5.3[35]. Напишите функцию, которая принимает число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя нацело: 1 и само число
# Если число простое - функция возвращает True, если нет - возвращает False
# Примеры/Тесты:
# <function_name>(13) -> True
# <function_name>(10) -> False
import math
def is_prime(number):
    for el in range(2, number):
        if number % el == 0:
            return False
    return True

print(is_prime(13))
print(is_prime(10))