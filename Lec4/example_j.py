# Решение задачи B

login = input()
email = input()

if len(login) <= 10 or "@" in login:
    print("Некорректный логин")
elif not("@" in email) or not ("." in email):
    print("Некорректная почта")
else:
    print("ОК")