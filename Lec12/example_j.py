# Решение задачи E

translation = {}
CLOSE_COMMAND = "Закрыть"
APPEND_COMMAND = "Добавить"
SHOW_COMMAND = "Показать"
WORD_NOT_FOUND = "Нет в словаре"

while True:
    command = input().strip()

    if CLOSE_COMMAND in command:
        break
    elif APPEND_COMMAND in command:
        n_operations = int(command.split()[-1]) # ["Добавить", "3"][-1]
        for _ in range(n_operations):
            words = input().strip().split() # ["milk", "молоко"]
            latin_word = words[0]
            russian_word = words[-1]
            translation[latin_word] = russian_word

    elif SHOW_COMMAND in command:
        n_operations = int(command.split()[-1]) # ["Показать", "3"][-1]
        for _ in range(n_operations):
            latin_word = input().strip()
            # if latin_word in translation.keys():
            #     print(translation[latin_word])
            # else:
            #     print(WORD_NOT_FOUND)
            print(translation.get(latin_word, WORD_NOT_FOUND))