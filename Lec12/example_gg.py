# Пример : счетчик символов в строке
# Пользователь вводит произвольную строку
# Задача: вывести на консоль сколько раз каждая буква входит
# в эту строку


message = "Hello world!"
counter = {}

for letter in message:
    if letter in counter.keys():
        counter[letter] = counter[letter] + 1 # counter["l"] = counter["l"] + 1 =2
    else:
        counter[letter] = 1 # counter["l"] = 1

for k, v in counter.items():
    print(k, v)