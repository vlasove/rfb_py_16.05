# Решение задачи T
cpp_set = set()
rust_set = set()

n_cpp = int(input())
m_rust = int(input())

for _ in range(n_cpp):
    cpp_set.add(input())

for _ in range(m_rust):
    rust_set.add(input())

result = cpp_set.symmetric_difference(rust_set)
print(len(result))