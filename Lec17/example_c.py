"""
example_c:
    Тщетные попытки достучаться до элементов
    модуля example_a
"""

from example_a import add, MAX_ATTEMPTS # 
# совмещаем (добавляем в текущее пространство имен) имена add, MAX_ATTEMPTS

# MAX_ATTEMPTS = 999999
# add = lambda x,y : x ** 2 - y ** 2


print(MAX_ATTEMPTS)
print(add(2,3))