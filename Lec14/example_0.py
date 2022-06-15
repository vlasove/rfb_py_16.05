"""
Примеры функций, возвращающих какие-либо значения
* Явный возврат не пустого значения
        * Сначала вычисляется выражение, стоящее справа от return
        * Затем данная конструкция прерывает выполнение тела функции
        * На вызывающую сторону отдается вычисленное значение
        * К телу функции больше нет доступа

* Функции в Python всегда возвращают что-то:
    * Если справа от return указано какое-то выражение - будет возвращен вычисленные результат
    * Если справа от return ничего нет ИЛИ return отсутсвует в теле функции - будет возвращаено None
"""

def square_sum(a, b):
    """
    Подсчитывает квадрат суммы аргументов
    """
    return abs((a  + b) ** 2)

def add(a, b):
    """
    Сложение аргументов, ничего не возвращает
    """
    result = a + b
    print(result)

def sub(a, b):
    """
    Разность аргументов
    """
    result = a - b
    if result % 2 == 0:
        print("Before empty return")
        return
    print(result)

def main():
    """
    entry point
    """
    x, y = 15, 10
    res = square_sum(x , y)
    print("Result square_sum is:", res)

    res2 = add(x, y)
    print("Result add is:", res2)

    res3 = sub(x, y)
    print("Result sub is:", res3)

    lst = [10, 20, 30, -1]
    res4 = lst.sort()

    # Проверка результата функции на None
    # Способ 1
    if res4 == None:
        print("Result sort:", res4)
        
    # Способ 2
    if res4 is None:
        print("Result sort:", res4)
        
    print(lst)

main()