# Синтаксис цикла for
# for expression:
#     body
# Простейший цикл for

# i = 1
# while i < 10:
#     print(i)
#     i += 1

# for j in range(1, 10, 1): #[start, stop), step]
#     print("Value:", j)

# range(start, stop, step)
# stop - это краевой параметр (т.е. итерации идут ДО НЕГО, не включая его самого)

for i in range(1, 10): # range(start, stop[, step=1)
    print("Another Value:", i)

# При итерировании в сторону увеличения ОБЯЗАТЕЛЬНО:
# * start < stop
# * step > 0
stopper = 15
for i in range(stopper): # range(start=0, stop[, step=1)
    print("Third Value:", i)

# При итерировании в сторону уменьшения ОБЯЗАТЕЛЬНО
# * start > stop
# * step < 0
for j in range(0, -10, -2): # start=0, stop[-10, step = 1
    print("Negative iterations:", j)

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
