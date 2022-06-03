# Пример. Считывание данных из входного потока
# numerics_str = input()
# list_numerics_str = numerics_str.split()
# numerics = []
# for elem in list_numerics_str:
#     numerics.append(int(elem))

# print(numerics)


numerics = [int(elem) for elem in input().strip().split()] # ["10", "20", "30", "40", ...]
print(numerics) # [10, 20, 30, 40, ..]

values = [1, 2, 3, 4, 88, 99, 100, 12]
values = [elem + 1 for elem in values]

print(", ".join([str(x) for x in values]))