# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

#     Примеры/Тесты:
#     4 4 -> 2 2
#     5 6 -> 2 3
# **Примечание.**
# Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение - посмотрите  в сети. Обойдите дополнительной проверкой возможность комплексных решений.
# Можно игнорировать то, что получаться рациональные решения вместо натуральных.
# Для вычисления квадратного корня используйте возведение в степень 0.5 или 
# **Усложнение.** найдите самостоятельно в сети какая функция стандартной библиотеки вычисляет квадратный корень и как до нее добраться.
# x + y = A
# x * y = B
# x = B / y
# B / y + y = A
# y^2 - A * y + B = 0
# D = A^2 - 4 * B = 0
# x = (A + sqrt(D)) / 2
# y = (A - sqrd(D)) / 2
import math

def Quadratic_equation(a, b):
    d = a ** 2 - 4 * b
    if d == 0:
        x = y = a / 2
    elif d < 0:
        print("Нет корней")
        return -1
    else:
        x = ((a + math.sqrt(d)) / 2)
        y = ((a - math.sqrt(d)) / 2)
    print(x, y)
    
a = int(input())
b = int(input())
Quadratic_equation(a, b)

