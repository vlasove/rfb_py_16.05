# Преобразования list <-> set
numerics_list = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]
numerics_set = set(numerics_list) # Преобразование из списка в множество
new_list = list(numerics_set) # Преобразование из множества в список

numerics_list = sorted(list(set(numerics_list)))
print(numerics_list)


# list <-> str
words = "Hello world"
letters = list(words)
print(letters)

print("".join(["10", "20"]))