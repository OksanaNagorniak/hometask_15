# Задание 6
# Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

with open ("task_6.txt", 'r') as f:
    summa = 0
    for line in f:
        for word in line.split():
            summa += int(word)
print(summa)