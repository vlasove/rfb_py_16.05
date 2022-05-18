# Неявное преобразование типов
a_int = 10
b_float = 12.5

res = a_int + b_float ** 2 # float(a_int) + b_float ** float(2)
print(res)

# Явное преобразование int<->float
value_int = 125
value_float = float(value_int)
print("Type:", type(value_float), "Value:", value_float)

second_value_int = int(12.9999999) # отбрасывается вся десятичная часть!
print("Type:", type(second_value_int), "Value:", second_value_int)


# Вывод вещственного числа с точностью
value = 817347.92843763281
print(f"Value: {value: .5f}")