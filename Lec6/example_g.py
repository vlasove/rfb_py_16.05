# Решение задачи S

from_home_to_park = set()
from_park_to_home = set()

# Наполняем множества - от дома до парка
while True:
    bus_num = input()
    if bus_num == "":
        break
    from_home_to_park.add(bus_num)

# Наполняем множества - от парка до дома
while True:
    bus_num = input()
    if bus_num == "":
        break
    from_park_to_home.add(bus_num)

# Выделяем общие автобусы
general = from_home_to_park.intersection(from_park_to_home)
print(len(general))