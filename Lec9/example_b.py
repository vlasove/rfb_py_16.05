# Методы преобразования str-list

# Строковый метод .split()
message = "Bob likes Python programming"
words = message.split(sep=" ") # sep='\s' =>' ' , '     ', '\t', '\n'
print("Words:", words)

# words = ['Bob', 'likes', 'Python', 'programming']
# Строковый метод .join() ---> sep.join(list[str])
output_str = ", ".join(words) # "Bob" + ", " + "likes" + ", " + "Python" + ", " + "programming"
print(output_str)

# list[str] - обязателен!
numerics = [1,2,3,4,5]
numercis_as_str = []
for num in numerics:
    numercis_as_str.append(str(num))

print(numercis_as_str)

print("\t".join(numercis_as_str))