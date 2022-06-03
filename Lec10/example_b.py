# Списочные выражения. Часть 1

# 1. Список из 100 нулей
zeros = [0] * 100 # [0] + [0] + [0] + [0] ... = [0, 0] + [0] + ... = [0,0,0] + [0] + ...
print("Zeros:", zeros)

# 2. Список из 100 первых натуральных чисел
numerics = []
for i in range(100):
    numerics.append(i)

print("Numerics:", numerics)

# 3. Список, построенный на первых 100 натуральных числах, с условием:
# *) Если число чётное - в список добавить его квадрат
# *) Если число нечётное - в список добавить его куб

new_numeric = []
for i in range(100):
    if i % 2 == 0:
        new_numeric.append(i ** 2)
    else:
        new_numeric.append(i ** 3)

print("New numerics:", new_numeric)