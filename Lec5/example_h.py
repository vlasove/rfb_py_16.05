# Старый алгоритм мин/макс
# Вам заранее известны возможные пределы вводимых значений!
# Напишем программу, которая будет принимать на вход целые положительные числа
# из диапазона [1,...,1000]
# Необходимо найти максимальное и минимальное из введенных значений

MIN_VALUE = 1001 # Больше любого введенного
MAX_VALUE = -1   # Меньше любого введенного

while True:
    numeric = int(input())
    if numeric <= 0:
        break

    if numeric < MIN_VALUE:
        print("Переопределение минимума:", numeric)
        MIN_VALUE = numeric

    if numeric > MAX_VALUE:
        print("Переопределение максимума:", numeric)
        MAX_VALUE = numeric


print("Минимум:", MIN_VALUE)
print("Максимум:", MAX_VALUE)