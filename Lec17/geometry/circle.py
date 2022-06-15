"""
Модуль пакета geometry
Содержащий набор функция для подсчета:
* площади окружности
* периметра окружности
"""
import math

def area(radius:float):
    """
    description
    """
    return math.pi * radius ** 2

def perimeter(radius:float):
    """
    description
    """
    return 2 * math.pi * radius
