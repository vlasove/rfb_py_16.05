# Решение задачи N
n = int(input())
numerics = []

for _ in range(n):
    numerics.append(int(input()))

lhs = int(input())
rhs = int(input())

print(sum(numerics[lhs-1:rhs]))


