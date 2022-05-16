# Логический тип
t_bool = True
f_bool = False

# Логическое умножение (and)
print(t_bool and t_bool)
print(t_bool and f_bool)
print(f_bool and t_bool)
print(f_bool and f_bool)

# Логическое сложение (or)
print(t_bool or t_bool)
print(t_bool or f_bool)
print(f_bool or t_bool)
print(f_bool or f_bool)

# Логическое отрицание (not)
print(not t_bool)
print(not f_bool)


# Неявное приведение в арифметических выражениях
print(True*2 + False**True)