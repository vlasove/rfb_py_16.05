# Обработка списков
nums = [ 10, 20, 30, 40, 50]
elems = [9, 99, 99, 9999]

# Конкатенация
print(nums + elems)
print(nums * 4)

# Проверка вхождения
if 20 in nums:
    print("20 in nums")

# Изменение списка
nums[0] = 100500
print(nums)

# min/max/sum
print("sum:", sum(nums[1:4]))
print("max:", max(nums))
print("min:", min(nums))