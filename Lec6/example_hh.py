# Ссылочность множеств
a_set = set([1, 2, 3, 4, 5]) # xb00000b00b0xa
# b_set = a_set
b_set = a_set.copy() # xb00000b124687s
b_set.add(100)

print("a_set:", a_set)
print("b_set:", b_set)