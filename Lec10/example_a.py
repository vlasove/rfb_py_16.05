# Тернарный условный оператор

numeric = None # Допустим это инициализирующее значение

if 10 % 2 == 0:
    numeric = 2
else:
    numeric = 5

print("Numeric:", numeric)



new_numeric = 2 if 10 % 2 == 0 else 5
#a = value1 if expression else value2
# # возвращает value1 если expression  -> True
# # в противном случае возвращает value2
print("New numeric:", new_numeric)