"""Модуль содержащий набор простейших арифметических функций, содержащий как их
реализацию, так и использование для вычисления нетривиального выражения."""
# import math
# import os
# import sys

# from flask import Flask
# from pandas import DataFrame

# import example_a


def add(x_arg: int, y_arg: int) -> int:
    """
    ОПИСАНИЕ:
        Арифметическое сложение аргументов
    ПАРАМЕТРЫ:
        x_arg ...
        y_arg ...
    РЕЗУЛЬТАТ:
        ...
    """
    return x_arg + y_arg


def sub(x_arg, y_arg) -> int:
    """
    ОПИСАНИЕ:
        Арифметическое вычитание аргументов
    ПАРАМЕТРЫ:
        x_arg ...
        y_arg ...
    РЕЗУЛЬТАТ:
        ...
    """
    return x_arg - y_arg


def mult(x_arg, y_arg) -> int:
    """
    ОПИСАНИЕ:
        Арифметическое умножение аргументов
    ПАРАМЕТРЫ:
        x_arg ...
        y_arg ...
    РЕЗУЛЬТАТ:
        ...
    """
    return x_arg * y_arg


def div(x_arg, y_arg) -> int:
    """
    ОПИСАНИЕ:
        Арифметическое целочисленное деление аргументов
    ПАРАМЕТРЫ:
        x_arg ...
        y_arg ...
    РЕЗУЛЬТАТ:
        ...
    """
    return x_arg // y_arg


def main() -> None:
    """Основная точка входа в приложение."""
    first_arg, second_arg = int(input().strip()), int(input().strip())
    result = (
        add(first_arg, second_arg)
        + add(second_arg, first_arg)
        + sub(add(first_arg, first_arg), mult(second_arg, second_arg))
        - div(second_arg, first_arg) ** 2
        + add(first_arg, second_arg)
        + add(second_arg, first_arg)
        + sub(add(first_arg, first_arg), mult(second_arg, second_arg))
        - div(second_arg, first_arg) ** 2
    )
    print(result)


if __name__ == "__main__":
    main()
