# Вещественные числа
a_float = float(input()) # float("5.5") => 5.5 - пример явного приведения типов (из строки в целое число)
b_float = float(input()) # float("3.5") => 3.5


print(f"A value {a_float} and B value {b_float}")
print("Type of A:", type(a_float))
print(a_float, b_float)

print("a - b = ", a_float - b_float)
print("a + b = ", a_float + b_float)
print("a * b = ", a_float * b_float)
print("a / b =", a_float / b_float) # Деление всегда вещественно-значное

print("a // b=", a_float // b_float) # Целочисленное деление
print("mod(a,b) = ", a_float % b_float) # Остаток от деления
print("a ^ b = ", a_float ** b_float) # a_float - основнаия, b_float - показатель степени