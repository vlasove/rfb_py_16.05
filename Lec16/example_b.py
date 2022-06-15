"""
Анонимные функции (lambda-выражения) - функции без имен (у них у всех одно и то же имя lambda)
"""

def add(first_arg:int, second_arg:int):
    """
    description
    """
    return first_arg ** 2 + second_arg ** 2



def main():
    """
    description
    """
    print("add type:", type(add))
    print("add val:", add)
    res1, res2 = add(1,2), add(2,3)
    print("Res1 + Res2:", res1 + res2)

    anon_add = lambda first_arg, second_arg: first_arg ** 2 + second_arg ** 2
    anon_res1, anon_res2 = anon_add(1,2), anon_add(2,3)
    print("AnonRes1 + AnonRes2:", anon_res1 + anon_res2)

    print(type(anon_add))
    print(anon_add)

    for i in range(1, 10):
        res = (lambda x, y: x + y)(i, i+1)
        print(res)
    
    # Синтаксис lambda выражений:
    # lambda args: returned_body
    # returned_body - возвращаемое значение (или выражение)
    # args - исключительно RP args
    # args - не аннотируются
    # отсутствует docstring

main()