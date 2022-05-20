# Примеры логических выражений построенных на числовых типах
a_int = 100
b_int = 200.5

# Сравнение 
print(" > ", a_int > b_int)
print(" < ", a_int < b_int)
print(" >= ", a_int >= b_int)
print(" <= ", a_int <= b_int)

print(0 == 0.0) # Сравнение вещественного и целого нулей
print(" == ", a_int == b_int)
print(" != ", a_int != b_int)

# Четное ли число 100?
print(100 % 2 == 0)

# # Комбинирование
print(" > and !=", (a_int > b_int) and (b_int != 15))