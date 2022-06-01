# Наполенение списка
numerics = []

# Добавление в конец
numerics.append(10)
numerics.append(20)
numerics.append(30)

print(numerics)
# [10, 20, 30].insert(0, 99) -> [x, 10, 20, 30] -> [99, 10, 20, 30]
# Добавление в начало (или проивзольное место)
numerics.insert(0, 99) # insert(id, elem)
numerics.insert(2, 9999999)
numerics.insert(10000000, "этой позиции нет") # если id=1000000 нет в списке - выполнится append()
print(numerics)