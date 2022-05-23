# Решение задачи F
a_coeff = float(input())
b_coeff = float(input())
c_coeff = float(input())

if a_coeff == 0:
    if b_coeff == 0:
        print("корней нет")
    else:
        print("один корень")
else:
    d = b_coeff ** 2 - 4 * a_coeff * c_coeff
    if d  > 0 :
        print("два корня")
    elif d == 0:
        print("один корень")
    else:
        print("корней нет")