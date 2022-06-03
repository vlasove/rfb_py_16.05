# Начало решения задачи B

COMMAND_TO_PUSH_BACK = "Кто последний?"
COMMAND_TO_PUSH_TO_HEAD = "Я только спросить!"

queue = []
n_commands = int(input().strip())

for _ in range(n_commands):
    command = input().strip()
    if COMMAND_TO_PUSH_BACK in command:
        # command = "Кто последний? Я - Кузнецов."
        # blocks = command.split(" - ") # ["Кто последний? Я", "Кузнецов."]
        # last_name = blocks[-1].split(".")[0] # "Кузнецов.".split(".") -> ["Кузнецов", ""][0] -> "Кузнецов"
        last_name = command.split(" - ")[-1].split(".")[0]
        queue.append(last_name)
    elif COMMAND_TO_PUSH_TO_HEAD in command:
        ....
    else: # Следующий!
        ....
