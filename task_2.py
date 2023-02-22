# Задание 2
# Запросить у пользователя текст и записать его в файл data.txt

f = open("data.txt", "a")
f.write(input())
f.close()
