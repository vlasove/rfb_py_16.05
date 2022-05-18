# Целые числа (Явное приведение к типу int)
a_int = int(input())
b_int = int(input())

print(f"A value {a_int} and B value {b_int}")
print("Type of A:", type(a_int))
print(a_int, b_int)

# Отрицательные числа
print(-a_int)
c_int = -a_int

print("a - b = ", a_int - b_int)
print("a + b = ", a_int + b_int)
print("a * b = ", a_int * b_int)
print("a / b = ", a_int / b_int) # Деление всегда вещественно-значное

print("a // b = ", a_int // b_int) # Целочисленное деление
print("mod(a,b) = ", a_int % b_int) # Остаток от деления
print("a ^ b = ", a_int ** b_int) # a_int - основание, b_int - показатель степени
print("|-5| = ", abs(-5))