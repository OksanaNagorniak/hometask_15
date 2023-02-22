# Задание 1
# Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers

with open("task_1.txt") as f:
    data = f.read()
numbers = [int(i) for i in data if i.isdigit()]
print(numbers)
