# Решение задачи О
n = int(input())
result = 0

for i in range(n): # (0, 1, 2)
    numeric = int(input())

    # result += numeric * ((-1) ** i)

    if i % 2 ==0:
        result += numeric
    else:
        result -= numeric

print(result)