# Решение задачи D

x_init = int(input())
y_init = int(input())

x_result = int(input())
y_result = int(input())

delta_x = x_init - x_result
delta_y = y_init - y_result

vertical_expression = abs(delta_x) == 1 and abs(delta_y) == 2
horisontal_expression = abs(delta_x) == 2 and abs(delta_y) == 1


if vertical_expression or horisontal_expression:
    print("ДА")
else:
    print("НЕТ")