# Добавление новых элементов (новых пар)
transition = {10: "ten"}
transition[12] = "twelve" # Добавление как ключа, так и значения!
print(transition)

print("10 is:", transition[10]) # Чтение значений из словаря по ключам
print("12 is:", transition[12])
# print("13 is:", transition[13]) # Ошибка! Т.к. пары с ключом 13 нет

transition[10] = "TEN" # Перезапись значения по существующему ключу 10
print(transition)
print(transition[10]) # Чтение из словаря по ключу 10