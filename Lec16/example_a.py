"""
Функциональный объект - ссылка на участок памяти,
где зарезервированы команды необходимые для ВЫЗОВА функции
"""

def add(first_arg:int, second_arg:int) ->int:
    """
    description
    """
    return first_arg** 2 + second_arg**2

def sub(first_arg:int, second_arg:int) ->int:
    """
    description
    """
    return first_arg - second_arg

def trivial_calc(first_arg:int, second_arg:int, func) -> int:
    """
    description
    """
    return func(first_arg, second_arg)

def choose_operation(sign:str):
    """
    description
    """
    if sign =="+":
        return add
    elif sign == "-":
        return sub
    else:
        return add

def main() -> None:
    """
    description
    """
    res = add(1, 2) # В переменной res - лежит РЕЗУЛЬТАТ ВЫЗОВА ФУНКЦИИ add с параметрами
    print('add(1,2):', res)
    func_obj = add # В переменной func_obj - ледит ССЫЛКА НА команды, необходимые для ВЫЗОВА функции
    print("Func obj:", func_obj)
    print("func_obj(2,3) ~ add(2,3) :", func_obj(2,3))
    
    func_list = [add, sub]
    for func in func_list:
        print(func(10, 20))

    print("trivial_calc(2,3, add):", trivial_calc(2,3,add))
    print("trivial_calc(2,3, sub):", trivial_calc(2,3,sub))

    res = choose_operation("+")
    print("Result choose operation:", res)
    print("Result of result:", res(12,13))

    print(choose_operation("+")(12, 13))
    print(choose_operation("-")(12, 13))

main()