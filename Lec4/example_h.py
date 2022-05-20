# Обсчет приоритетов при вычислении логического выражения

age = int(input("age for and: "))

if age > 12 and 1/0: # and ЕСЛИ первое условие НЕВЕРНОЕ, тоо стальные даже не обсчитываются
    print("It's ok! (and)")

print("Done!")

age = int(input("age for or: "))
if age > 12 or 1/0: # or ЕСЛИ первое условие ВЕРНО, то отслаьные считать нет смысла, т.к. or Будет True
    print("It's ok! (or)")