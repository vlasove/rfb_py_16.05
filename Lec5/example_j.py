# Синтаксис цикла for
# for expression:
#     body

# Простейший цикл for

# i = 1
# while i < 10:
#     print(i)
#     i += 1

for i in range(1, 10, 1): #[start, stop)
    print("Value:", i)

# range(start, stop, step)
# stop - это краевой параметр (т.е. итерации идут ДО НЕГО, не включая его самого)

for i in range(1, 10): # range(start, stop[, step=1)
    print("Another Value:", i)

for i in range(10): # range(start=0, stop[, step=1)
    print("Third Value:", i)

# Важное ограничение - start/stop/step - всегда int

# break/continue
for i in range(1, 13, 1):
    if i > 11 :
        print("break!")
        break
    if i % 2 == 0:
        print("continue!")
        continue
    print("Curr value:", i)
