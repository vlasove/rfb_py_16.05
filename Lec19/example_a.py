"""
Считывание файла целиком
"""

# import pathlib

fh = open(file="input.txt", mode="r")
# print("file handler:", type(fh))
# print("file handler value:", fh)

content = fh.read()
print("Content:", content)
content2 = fh.read() # Потворное считывание продолжается с момента остановки предыдущего
print("Content 2:", content2)

fh.close()

# content = """
# Lorem ipsum dolor sit amet, 
# consectetur adipiscing elit, sed do 
# eiusmod tempor incididunt ut labore et dolore 
# magna aliqua. Ut enim ad minim veniam, 
# quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
# consequat. Duis aute irure dolor in reprehenderit in 
# voluptate velit esse cillum dolore eu fugiat nulla 
# pariatur. Excepteur sint occaecat 
# cupidatat non proident, sunt in culpa 
# qui officia deserunt mollit anim id est laborum.
# """