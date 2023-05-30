# №4.1[25]. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Примеры/Тесты:
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Input: a b c d a a a a a a a
# Output: a b c d a_1 a_2 a_3 a_4 a_5 a_6 a_7
# Строку не обязательно вводить с клавиатуры

input = "a a a b c a a d c d d"
output = []
count = dict()
for i in input:
    if i != ' ':
        if count.get(i) != None:
            count[i] += 1
            output.append(f"{i}_{count.get(i)}")
        else:
            count[i] = 0
            output.append(i)
print(' '.join(output))