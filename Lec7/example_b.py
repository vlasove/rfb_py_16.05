# Решение задачи H
word = input()
yes_set = set(["да", "Да" , "ДА", "дА", "ад", "Ад", "аД", "АД"])
yes = word[0] + word[-1]

if yes in yes_set:
    print("СОГЛАСЕН")
else:
    print("НЕ СОГЛАСЕН")