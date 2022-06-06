num_tuple = (10, 20, 30, 40 ,50)
# num_tuple[0] = 100 # Не получится - кортеж не изменяемый!

nums = [0] * 10
nums_tuple = (0,) * 10

print(nums)
print(nums_tuple)


# Явные преобразования коллекций tuple <-> list
nums_from_tuple = list(nums_tuple) # Преобразуем кортеж к списку
nums_from_list = tuple(nums) # Преобразуем список к кортежу