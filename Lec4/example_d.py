# Условный оператор с блоком else
# if expression:
#     body1
# else:
#     body2

point = int(input())

if abs(point) <= 25: # |point| <= 25
    print("Точка на отрезке!")
    print("Вторая строка")
else:
    print("Точка отрезку не принадлежит!")
    print("Что-то еще")

print("End of program")