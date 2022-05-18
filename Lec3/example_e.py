# Строки как базовый тип
name_str = "Bobby"
last_name_str = "Kotik"
third_name = 'The "Third"'

# Конкатенация
res = name_str + " " + last_name_str + " " + third_name # результат - новая строка!
print(res)

# Мультипликативная конкатенация (синтаксический сахар)
result = name_str * 5 # name_str + name_str + name_str + name_str + name_str
print(result) # Имеет смысл только при умножении на натуральное число

# Взятие длины
len_of_name = len(third_name)
print("Len:", len_of_name)

# Нет типа char, есть только str
character_example = 'a'
print("Type:", type(character_example))

# Пример считывания строки из входного потока
name = input()