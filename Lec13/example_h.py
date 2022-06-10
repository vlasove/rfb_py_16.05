"""
Решение задачи I
"""
def factorial(n):
    res = 1
    if n <= 1:
        return res

    for i in range(2, n+1):
        res *= i 
    return res

def combination(n, m):
    """
    """
    return factorial(n) // (factorial(m) * factorial(n -m))


n = int(input())
m = int(input())

result = combination(n, m)

print(result)