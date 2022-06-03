# Ссылочность коллекций
a_int_list = [10, 20, 30, 40] # на самом деле в переменной хранится ССЫЛКА на область памяти, гле лежат значения
b_int_list = a_int_list # [:] #.copy() 

# b_int_list = b"xafsg001axf001"
# a_int_list = b"xafsg001fax007"

b_int_list[0] = 100500

print("List a:", a_int_list)
print("List b:", b_int_list)


# Множество
a_set = set([1,2,3,4]) # здесь также в переменной хранится ссылка!
b_set = a_set #.copy()
# a_set = b"xf000xf"
# b_set = b"xf000xf"

b_set.add(100500)

print("Set a:", a_set)
print("Set b:", b_set)

# Строки - тоже ссылки, но только с доступом на чтение!
a_str = "Hello world!"
b_str = a_str