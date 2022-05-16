# Форматирование строк и изменение стандартного поведения print()
name = "Bobby"
last_name = "Johnson"
age = "25"

# Форматированные строки - f-strings
message = f"Hello! My name is '{name}', my lastname is !{last_name}!, age is {age}"
print(message)

# Еще один пример
word_a = "###"
word_b = "$$$"
word_c = "@@@"

new_message = f"{word_a}{word_b}{word_c}"
print(new_message)

# Изменение стандартных параметров print()
print("=======НЕПОВТОРИМЫЙ ОРИГИНАЛ============")
print("a", "b", "c")
print("d", "e", "f")
print("=======ЖАЛКАЯ ПОРОДИЯ===================")
print("a", "b", "c", sep=",", end="!!IT'S NEW LINE!!")
print("d", "e", "f", sep="!", end="\n")