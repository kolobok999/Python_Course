# №2.4[15]. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Затем пользователь последовательно вводит массы соответсвующих арбузов
# Необходимо вывести на экран массы самого тяжелого и самого легкого арбузов
# Примеры/Тесты:
# Введите кол-во арбузов>? 8
# Введите массу арбуза 1>? 12
# Введите массу арбуза 2>? 9
# ...
# 8 12 7 6 15 17
# Массы арбузов: min=6, max=17
while True:
    n = input("Введите кол-во арбузов: ")
    if n.isdigit(): 
        n = int(n)
        break
    else: print("Это не число")
max_watermelon_mass = 0
min_watermelon_mass = 999999
i = 1
while i <= n:
    watermelon_mass = input(f"Введите массу арбуза {i}: ")
    if watermelon_mass.isdigit(): watermelon_mass = int(watermelon_mass)
    else: 
        print("Это не число")
        break
    max_watermelon_mass = max(watermelon_mass, max_watermelon_mass)
    min_watermelon_mass = min(watermelon_mass, min_watermelon_mass)
    i += 1
print(f"Массы арбузов: min = {min_watermelon_mass}, max = {max_watermelon_mass}")
