# Оператор множетсвенного выбора (switch/select - отсутствуют)

# if expression1:
#     body1
# elif expression2:
#     body2
# elif expression3:
#     body3
# ...
# else:
#     body_else

age = int(input())

if age <= 14: # Читается сверху-вниз, первый правильный и будет выполнен
    print("Age <= 14")
elif age >= 15 and age <= 18:
    print("Age in [15, 18]")
elif age > 18 and age <= 45:
    print('Age in [19, 45]')
else: # необязательный блок
    print("Age is large")

print("Done")