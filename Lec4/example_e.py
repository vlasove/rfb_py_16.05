# Вложенный условный оператор (синтетический пример)
age = int(input())
name = input()

if age >= 18:
    print("Your age >= 18")
    print("Second Line")
    if name == "Vasya":
        print("Your name is Vasya")
        print("Another Line")
    else:
        print("Your name is not Vasya")
else:
    print("Your age < 18!!!")

print("Done!")