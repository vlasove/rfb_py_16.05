"""
example_b:
    Тщетные попытки достучаться до элементов
    модуля example_a
"""

import example_a as ex # импортирование с РАЗДЕЛЯЮЩИЕЙ ОБЛАСТЬЮ


MAX_ATTEMPTS = 999999
add = lambda x,y : x ** 2 - y ** 2

# print(ex, dir(ex)) - ex - тоже объект с методами и атрибутами
print(ex.MAX_ATTEMPTS)
print(ex.add(2, 3))


print(MAX_ATTEMPTS)
print(add(2,3))


