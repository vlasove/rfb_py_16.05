"""
Считывание всех строк в виде списка
"""

fh = open(file="input.txt", mode="r")
lines = fh.readlines()
print(lines)
for line in lines:
    print(line.strip())
fh.close()

# или с with

with open(file="input.txt", mode="r") as fh:
    lines = fh.readlines()
    print("All lines:", lines)
    for line in lines:
        print(line.strip())