"""
пример игнорирования default value arg
"""

def add(x_arg = 1, y_arg = 2, z_arg =3):
    """
    description
    """
    return x_arg + y_arg + z_arg

def main():
    """
    entry point
    """
    print(add(x_arg=5, z_arg=5))

main()