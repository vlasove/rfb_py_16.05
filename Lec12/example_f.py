# Методы словарей
words = {"one" : "один" , "two" : "два", "three" : "три", "four" : "четыре"}
# print(dir(words))

my_personal_key = "one"

# По умолчанию при использовании in dict поиск идет по ключам словаря!
if my_personal_key in words: # .keys():
    print(f"Key: {my_personal_key} Val:{words[my_personal_key]}")
else:
    print(None)


# Метод .get()
value = words.get(my_personal_key)
print(".get():", value)

# Метод .get() с значением по умолчанию
birthdays = {"jan" : 0, "feb" : 5, "mar" : 3}
month = "dec"
print("birthdays['dec']:", birthdays.get(month, 0))
print(birthdays)

# Метод .setdefault() аналогичен .get(), только в случае отсутсвия ключа в словаре
# добавит новую пару (month:10)
result = birthdays.setdefault(month, 10)
print('Result:', result)
print("After setdefault():", birthdays)

# Метод .fromkeys([keys], value]) позволяет инициализировать словарь
# из итерируемой коллекции ключей [keys] (значения у всех одинаковые value)
new_dict = {}
keys = ["a", "b", "c", "d"]
new_dict = new_dict.fromkeys(keys, 0)
print("After .fromkeys():", new_dict)

# Удаление пар из словаря
if "two" in words.keys():
    words = {"one" : "один" , "two" : "два", "three" : "три", "four" : "четыре"}
    del words["two"]
    print(words)

if "one" in words.keys():
    val = words.pop("one")
    print(words)
    print("Deleted one:", val)