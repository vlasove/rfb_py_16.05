# Удаление элементов из списка

# Через метод .pop()
elem = None
numerics = [ 10, 20, 30, 40, 50, 100, 50]
if len(numerics) != 3:
    elem = numerics.pop(2) # Удаляет последний по умолчанию, если передан индекс- удалит по индексу
print("Elem deleted:", elem)
print("Numerics:", numerics)

# Через метод .remove()
if 50 in numerics:
    for _ in range(numerics.count(50)):
        numerics.remove(50) # удаление по значению!
    print("After .remove():", numerics)

# del
del numerics[0]
print("After del:", numerics)