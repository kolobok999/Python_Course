# №2.3[13]. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# Затем пользователь последовательно вводит температуру для каждого дня. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Необходимо вычислить длительность самой длинной оттепели
# Примеры/Тесты:
# Введите число рассматриваемых дней>? 11
# Введите среднесуточную температуру для дня 1>? 1
# Введите среднесуточную температуру для дня 2>? 7
# ...
# 1 7 3 -1 -2 1 2 3 4 5 6
# -> Максимальная длительность 6дн
# Введите число рассматриваемых дней>? 6
# Введите среднесуточную температуру для дня 1>? -1
# Введите среднесуточную температуру для дня 2>? 2
# ...
# -1 2 3 4 -1 -2
# -> Максимальная длительность 3дн
while True:
    n = input("Введите число рассматриваемых дней N (1 ≤ N ≤ 100): ")
    if n.isdigit(): 
        n = int(n)
        if n >= 1 and n <= 100:
            break
    print("Введённое значение не соответствует условию")

max_streak = 0
current_streak = 0
for i in range(n):
    temperature = input(f"Введите среднесуточную температуру для дня {i + 1}: ")
    if temperature == "":
        print("Ввод прерван!")
        break
    temperature = int(temperature)
    if temperature > 0:
        current_streak += 1
    else:
        current_streak = 0
    if max_streak < current_streak:
        max_streak = current_streak
print(f"Максимальная длительность {max_streak} дн")