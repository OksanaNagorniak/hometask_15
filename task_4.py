# Задание 4
# Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt,
# где одна строка = одно число

import random
i = 0
numb_lst = []
while i < 100:
    number = random.randint(0, 101)
    numb_lst = numb_lst + [number]
    i = i+1

f = open('random_numbers.txt', 'w')
for i in numb_lst:
    s = str(i)
    f.write(s + "\n")
f.close()
