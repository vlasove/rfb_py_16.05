"""
Аргументы со значением по умолчанию (Default Values Args)
"""

def add(a = 0, b = 0):
    print("a is:", a)
    print("b is:", b)
    return a ** 2 + b ** 3

def shift(shifting, x_arg = 0.0, y_arg = 0.0):
    """
    shifting - абсолютное значение сдвига (обязательный параметр)
    x_arg, y_arg - начальные координаты до сдвига (необязательные параметры, по умолчанию 0.0)

    возвращает кортеж (x_arg + shift, y_arg + shift)
    """
    return (x_arg + shifting, y_arg + shifting)

def main():
    """
    входная точка в приложение
    """
    print(add())
    print(add(1))
    print(add(b = 10))
    print(add(1,2))
    # print(add(1,2,3))
    
    x, y = shift(5,y_arg = 10)
    print(f"X:{x}, Y:{y}")

main()