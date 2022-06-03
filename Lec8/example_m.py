# Входные данные не всегда такие, как вам кажутся
name = "Alice \n\n\t" # То что вводит в форму/в консоль/в файл
target_name = "alice" # то что лежит в базе

if target_name == name.strip().lower(): # "alice" ==? "alice"
    print('Same names')
else:
    print(
        f"Different names: first {target_name} and first len {len(target_name)};\n last {name} and len {len(name)}"
        )


# Теперь всегда, когда будет читать что-то из входного потока
value = input().strip() # int(input().strip())
numeric = int(input().strip()) # "10\t\n\t\n   \t"