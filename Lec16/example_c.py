"""
Функциональный объект - ссылка на участок памяти,
где зарезервированы команды необходимые для ВЫЗОВА функции
"""



def trivial_calc(first_arg:int, second_arg:int, func):
    """
    description
    """
    return func(first_arg, second_arg)

def choose_operation(sign:str, *args):
    """
    description
    """
    if sign =="+":
        return args[0]
    elif sign == "-":
        return args[1]
    else:
        return args[0]

def main():
    """
    description
    """
    func_obj = lambda x,y: x+y # В переменной func_obj - ледит ССЫЛКА НА команды, необходимые для ВЫЗОВА функции
    print("Func obj:", func_obj)
    print("func_obj(2,3) ~ add(2,3) :", func_obj(2,3))
    
    func_list = [lambda x,y: x + y, lambda x,y: x - y]
    for func in func_list:
        print(func(10, 20))

    print("trivial_calc(2,3, add):", trivial_calc(2,3,lambda x,y: x + y))
    print("trivial_calc(2,3, sub):", trivial_calc(2,3,lambda x,y:x-y))

    print(choose_operation("+", lambda x,y: x + y, lambda x,y: x - y)(12, 13))
    print(choose_operation("-", lambda x,y: x + y, lambda x,y: x - y)(12, 13))

main()