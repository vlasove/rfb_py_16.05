# Вещественные числа
a_float = float(input())
b_float = float(input())


print(f"A value {a_float} and B value {b_float}")
print("Type of A:", type(a_float))
print(a_float, b_float)

# Отрицательные числа
print(-a_float)
c_float = -a_float

print("a - b = ", a_float - b_float)
print("a + b = ", a_float + b_float)
print("a * b = ", a_float * b_float)
print("a / b =", a_float / b_float) # Деление всегда вещественно-значное

print("a // b=", a_float // b_float) # Целочисленное деление
print("mod(a,b) = ", a_float % b_float) # Остаток от деления
print("a ^ b = ", a_float ** b_float) # a_float - основнаия, b_float - показатель степени
print("|-5.2| = ", abs(-5.2))