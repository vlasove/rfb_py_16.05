# Решение задачи N
# n! = 1 * 2 * 3 * 4 * 5 * .. * n
# 1! = 1
# 0! = 1

result = 1
n = int(input())

if n <= 1:
    print(result)
else:
    for i in range(2, n + 1):
        result *= i
    print(result)