# Ссылочность словарей
d = {"a":1, "b":2}
# Метод копирования словарей
new_d = d.copy() 
new_d["a"] = 100

print("Origin:", d)
print("Second:", new_d)

# Очистка словаря
new_d.clear()
print(new_d)

print(dir(new_d))