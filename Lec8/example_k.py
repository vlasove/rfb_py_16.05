# Сортировка списков
# Для того, чтобы список(или срез списка) можно было отсортировать
# необходимо чтобы элементы этого списка были попарно сравнимы

# Существует 2 способа сортировки
numerics = [10, 2, 3, 100, -2, -100, 3, 4, 17, 2, 99, -5]
# 1-ый способ: с изменением оригинального списка
numerics.sort() # -> None
print("numerics.sort():", numerics)
numerics.sort(reverse=True) # Обратная сортировка
print("numerics.sort(reverse=True):", numerics)

# 2-ой способ: с созданием нового списка и его последующей сортировкой (оригинальный при этом не меняется)
another_numerics = [10, 2, 3, 100, -2, -100, 3, 4, 17, 2, 99, -5]
sorted_numerics = sorted(another_numerics, reverse=True)
print("Origin:", another_numerics)
print("Sorted():", sorted_numerics)

# Сортировка строк
names = ["bob", "alice", "dan", "alex"]
names.sort()
print(names)