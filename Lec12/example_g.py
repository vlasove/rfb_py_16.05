# Работа с ссылочными типами в качестве занчений словаря
data = {
    "name" : "TestUser", 
    "last_name" : "TestUserInfo", 
    "targets" : [1,2,3,4,1,2] # b'xasdxzasd1320101'
    }

for t in data["targets"]: # link to [1, 2, 3, 4, 1, 2]
    print(t)

# Добавить новое действие
# tar = data["targets"] # link to [1, 2, 3, 4, 1, 2]
data["targets"].append(8)
data["targets"].remove(2)

print("Data:", data)
