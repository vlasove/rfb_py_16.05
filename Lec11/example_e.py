# Если кортеж хранит ссылочные типы - неизменяемост будет
# касаться только хранимых ссылок (фактических значений ссылок), а не их содержимого

nums = (
    [1,2,3], 
    [10, 20, 30]
)

print("0-th:", nums[0])
nums[0].append(1000)
print(nums)
