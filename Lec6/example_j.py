# Решение задачи C
n_cpp = int(input()) # |A|
m_rust = int(input()) # |B|

students = set()

for _ in range(n_cpp + m_rust):
    students.add(input()) # A u B

result = 2 * len(students) - n_cpp - m_rust
print(result)