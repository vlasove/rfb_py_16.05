CLOSE_COMMAND = "exit"

def run():
    while True:
        command = input().strip()
        if command == CLOSE_COMMAND:
            print("SERVER SUCCESSFULLY CLOSED")
            return