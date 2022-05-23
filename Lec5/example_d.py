# Решение задачи H

while True:
    word = input()
    if word == "": # терминальное условие
        break
    print(word)


# Часть решения задачи I

while True:
    first_password = input()
    second_password = input()

    if len(first_password) < 8:
        print("......")
    elif "123" in first_password or "qwe" in first_password:
        print("....")
    elif first_password != second_password:
        print("..........")
    else:
        print("Ну наконец-то!")
        break