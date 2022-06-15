"""
Пример использования пакета geometry
Пакет - группа модулей, схожих по своему функционалу (дополняющих друг друга)
__init__.py - модуль, который подскажет интерпретатору, что перед ним ТОЧНО пакет
"""
from geometry import rectangle as rect
from geometry.circle import perimeter, area

# Работа с прямоугольником
a, b = 10, 20
print(f"Периметр ({a}, {b}):", rect.perimeter(a,b))
print(f"Площадь ({a}, {b}):", rect.area(a,b))
# Работа с окружностью
r = 35.5

print(f"Преиметр окружности ({r}):", perimeter(r))
print(f"Площадь окружности ({r}):", area(r))