# Простой калькулятор
# Принимает на вход 2 вещественных числа и знак арифметической операции
# Поддерживаемые знаки: +, -, *
# В случае, если введенная операция поддерживается - вывести на консоль результат этой опреации
# В случае, если операция не поддерживается - вывести "НЕ ПОДДЕРЖИВАЕТСЯ"

a_float = float(input())
b_float = float(input())
sign = input()

if sign == "+":
    print(a_float + b_float)
elif sign == "-":
    print(a_float - b_float)
elif sign == "*":
    print(a_float * b_float)
elif sign == "/" and b_float != 0:
    print(a_float / b_float)
else:
    print("СБОЙ")