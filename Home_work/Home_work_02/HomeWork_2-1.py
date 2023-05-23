# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
#     Примеры/Тесты:
#     Введите кол-во монет>? 5
#     Положение монеты 0: 0 или 1>? 1
#     ...
#     1 0 1 1 0
#     Кол-во монет, чтобы перевернуть: 2

while True:
    n = input("Введите кол-во ионет: ")
    if n.isdigit(): 
        n = int(n)
        break
    else: print("Это не число")

head = 0 #1
tail = 0 #0
i = 1
while i <= n:
    current_side = input(f"Положение монеты {i}: 0 или 1?: ")
    if current_side.isdigit(): current_side = int(current_side)
    else: 
        print("Это не число")
        continue
    if current_side == 1: head +=1
    else: tail +=1
    i += 1
print(f"Кол-во монет, чтобы перевернуть: {head if head < tail else tail}")