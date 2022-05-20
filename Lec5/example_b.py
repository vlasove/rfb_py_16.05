# Условно-бесконечный цикл while

while True:
    password = input()
    if len(password) > 10:
        print("Password is valid!")
        break
    else:
        print("Invalid password. Try again!")

# break - операторное слово, которое может быть использовано ТОЛЬКО в теле цикла (или вложено в его часть),
# которое, ОСТАНАВЛИВАЕТ ТЕКУЩУЮ ИТЕРАЦИЮ И ПЕРЕДАЕТ УПРАВЛЕНИЕ ПЕРВОЙ КОМАНДЕ, СТОЯЩЕЙ ЗА ПРЕДЕЛЕАМИ ЦИКЛА!

# continue - -//- ОСТАНАВЛИВАЕТ ТЕКУЩУЮ ИТЕРАЦИЮ И ПЕРЕДАЕТ УПРАВЛЕНИЕ СЛЕДУЮЩЕЙ ИТЕРАЦИИ!
print("Done!")

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    else:
        print("I is odd:", i)
    print("Another line")
