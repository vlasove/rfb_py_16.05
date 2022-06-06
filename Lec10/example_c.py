# Списочное выражение. Часть 2

# Синтаксис
# 1.[elem for elem in iter]
# 2.[elem for elem in iter if expression]
# 3.[elem if expression else elem+1 for elem in iter]

# 1.[elem for elem in iter]
numerics = [i for i in range(100)]
print("Numerics:", numerics)

zeros = [0 for _ in range(100)]
print("Zeros:", zeros)

# Списочные выражения проще всего читать справа налево

# [i**2 + 1 for i in range(10)]
# Pyt: range, скажи пожалуйста, сколько раз ты собираешься отдать значение?
# range: 10
# Pyt: Принято
# to_return = [None, None, None, None, None, None, ..., None] - длины 10
# Pyt: выполним 0-ую итерацию
# Получилось значение: 0**2 + 1 = 1
# Pyt: to_return[0] = 1

# Pyt: выполним 1-ую итерацию
# Получилось занчение 1**2 + 1 = 2
# Pyt: to_return[1] = 2
# ....

# 2.[elem for elem in iter if expression]
# Создадим список только из натуральных четных чисел
even_numerics = [i for i in range(100) if i % 2 == 0]
print("Even Numerics:", even_numerics)

# 3.[elem if expression else elem+1 for elem in iter]
sharding_indexes = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(100)]
print("Sharding Indexes:", sharding_indexes)
