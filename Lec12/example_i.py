# Решение задачи D

birthdays = {
    "янв" : [],
    "фев" : [],
    "мар" : [],
    "апр" : [],
    "май" : [],
    "июн" : [],
    "июл" : [],
    "авг" : [],
    "сен" : [],
    "окт" : [],
    "ноя" : [],
    "дек" : [],
}

n = int(input().strip()) # Количество друзей для добавления в книгу
for _ in range(n):
    name, _, month = input().strip().split() # "Вася 10 май" -> ["Вася", "10", "май"]
    birthdays[month].append(name)

m = int(input().strip()) # Количество запросов к книге
for _ in range(m):
    names_in_month = birthdays[input().strip()]
    if len(names_in_month) == 0:
        print()
    else:
        print(" ".join(sorted(names_in_month)))