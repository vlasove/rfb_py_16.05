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

# Удаление пар из словаря
words = {"one" : "один" , "two" : "два", "three" : "три", "four" : "четыре"}
del words["two"]
print(words)

val = words.pop("one")
print(words)
print("Deleted one:", val)