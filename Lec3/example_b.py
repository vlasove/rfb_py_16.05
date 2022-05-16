# Целые числа
a_int = int(input()) # int("5") => 5 - пример явного приведения типов (из строки в целое число)
b_int = int(input()) # int("3") => 3


print(f"A value {a_int} and B value {b_int}")
print("Type of A:", type(a_int))
print(a_int, b_int)

print("a - b = ", a_int - b_int)
print("a + b = ", a_int + b_int)
print("a * b = ", a_int * b_int)
print("a / b =", a_int / b_int) # Деление всегда вещественно-значное

print("a // b=", a_int // b_int) # Целочисленное деление
print("mod(a,b) = ", a_int % b_int) # Остаток от деления
print("a ^ b = ", a_int ** b_int) # a_int - основнаия, b_int - показатель степени