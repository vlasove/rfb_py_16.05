# Великие секреты мастеров :)
def add(x,y):
    return x + y

a = lambda x,y: x+y
b = lambda x,y: x **2 + y**2

# Условимся:
# * для сортировки будем использовать ФО принимающие 2 целых числа и возвращающих 1 целое число
# * бОльшим ФО будем считать тот, который на значения 1 и 2 покажет бОльший результат
# * запрещено делать явный вызов на уровне использования списка ФО

urodstvo = [b, add, a]
urodstvo.sort(key=lambda f: f(1,2))
print(urodstvo)

for func in urodstvo:
    print(func(10, 20))


# Явную функцию можно создать без параметров
def empty():
    pass

# Вопрос: возможно ли создать анонимку без параметров?
print(lambda : None)

# Можно определять функции одну внутри другой (замыкание)
def add(a,b):
    def super_add(a,b,c):
        return a + b + c
    return super_add(a,b, 100)

lambda x,y: (lambda x,y,z: x+y+z)(x,y,100)