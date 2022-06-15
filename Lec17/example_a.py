"""
example_a:
    Пример модуля с:
    * явной функцией (1 шт)
    * переменной (1 шт)
    * каким-то куском кода, который использует функцию и переменную
"""
# import example_b as ex
# print(ex.MAX_ATTEMPTS)

def add(x_arg:int, y_arg:int):
    """
    Сложение вида x^3 + y ^4
    """
    return x_arg ** 3 + y_arg ** 4


MAX_ATTEMPTS = 10

def run():
    for i in range(MAX_ATTEMPTS):
        print("Res:", add(i, i + MAX_ATTEMPTS))
        if i > 3 :
            break

if __name__ == '__main__':
    run()