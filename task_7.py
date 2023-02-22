# задание 7
# Дан файл в котором записан текст,
# необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
from collections import Counter
common_words = []
with open("task_5.txt") as f:
    counter = Counter(f.read().split())
    common_words = counter.most_common(5)
print('\n '.join(map(str, common_words)))

