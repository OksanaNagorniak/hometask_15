# Задание 3
# Запросить у пользователя число N и запросить N чисел у пользователя,
# потом записать их в файл numbers.txt через пробел
from typing import List

list_numbers = []
N = int(input("Введите количество раз ввода чисел: "))
for i in range(N):
    numbers = int(input("Введите число: "))
    list_numbers.append(numbers)

f = open('numbers.txt', 'w')
for i in list_numbers:
    s = str(i)
    f.write(s + " ")
f.close()

