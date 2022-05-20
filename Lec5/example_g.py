# Сумма / произведение в виде внешнего счетчика
summ = 0
mult = 1

while True:
    numeric = int(input())
    if numeric <= 0:
        break

    summ += numeric
    mult *= numeric

print("Общая сумма:", summ)
print("Общее произведение:", mult)