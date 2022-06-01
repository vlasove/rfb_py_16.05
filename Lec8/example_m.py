# Входные данные не всегда такие, как вам кажутся
name = "Alice \n\n\t" # То что вводит в форму/в консоль/в файл
target_name = "alice" # то что лежит в базе

if target_name == name.lower().strip(): # "alice" == "alice "
    print('Same names')


# Теперь всегда, когда будет читать что-то из входного потока
value = input().strip() # int(input().strip())