"""Модуль содержащий набор простейших арифметических функций, содержащий как их
реализацию, так и использование для вычисления нетривиального выражения."""


def add(first_arg: int, second_arg: int) -> int:
    """
    ОПИСАНИЕ:
        Арифметическое сложение аргументов
    ПАРАМЕТРЫ:
        x_arg ...
        y_arg ...
    РЕЗУЛЬТАТ:
        ....
    """
    return first_arg + second_arg


def sub(first_arg: int, second_arg: int) -> int:
    """
    ОПИСАНИЕ:
        Арифметическое вычитание аргументов
    ПАРАМЕТРЫ:
        x_arg ...
        y_arg ...
    РЕЗУЛЬТАТ:
        ....
    """
    return first_arg - second_arg


def mult(first_arg: int, second_arg: int) -> int:
    """
    ОПИСАНИЕ:
        Арифметическое умножение аргументов
    ПАРАМЕТРЫ:
        x_arg ...
        y_arg ...
    РЕЗУЛЬТАТ:
        ....
    """
    return first_arg * second_arg


def div(first_arg: int, second_arg: int) -> int:
    """
    ОПИСАНИЕ:
        Арифметическое целочисленное деление аргументов
    ПАРАМЕТРЫ:
        x_arg ...
        y_arg ...
    РЕЗУЛЬТАТ:
        ....
    """
    return first_arg // second_arg


def main() -> None:
    """Основная точка входа в приложение."""
    num_a, num_b = int(input().strip()), int(input().strip())
    result = (
        add(num_a, num_b)
        + add(num_b, num_a)
        + sub(add(num_a, num_a), mult(num_b, num_b))
        - div(num_b, num_a) ** 2
        + add(num_a, num_b)
        + add(num_b, num_a)
        + sub(add(num_a, num_a), mult(num_b, num_b))
        - div(num_b, num_a) ** 2
    )
    print(result)


if __name__ == "__main__":
    main()
