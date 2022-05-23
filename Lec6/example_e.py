# Решение задачи R
n_words = int(input())
words = set()

for _ in range(n_words):
    words.add(input())

new_word = input()
if new_word in words:
    print("НЕ ЗАСЧИТАНО")
else:
    print("ЗАСЧИТАНО")