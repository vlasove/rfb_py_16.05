# Потоком ввода стандартный (STDIN)
# input() -> всегда возвращает строку

# name = input() # "Alice and Bob"
# print("My name is:", name)

name = input()
last_name = input()
age = input()

message = f"Имя: {name} , Фамилия: {last_name} , Возраст: {age} . Студент BPS"
print(message)