# Обработка множеств
numeric_set = set([10, 20, 30, 22.5, 12, 45, 32.5, -10])

total_sum = sum(numeric_set) # Если множество ТОЛЬКО из числовых типов (или приводимых к ним)
print("Sum:", total_sum)

min_num = min(numeric_set) # Если множество состоит только ИЗ СРАВНИМЫХ МЕЖДУ СОБОЙ элементов
print("Min:", min_num)

max_num = max(numeric_set)
print("Max:", max_num)

# Перебор элементов множества при помощи for
for elem in numeric_set: # Цикл for each
    print("Elem:", elem)