# Решение задачи A

n_dishes = int(input().strip())
dishes = []

for _ in range(n_dishes):
    dishes.append(input().strip())

n_days = int(input().strip())

for _ in range(n_days):
    dish_amount = int(input().strip())
    for _ in range(dish_amount):
        dish = input().strip()

        if dish in dishes:
            dishes.remove(dish)

for dish in sorted(dishes):
    print(dish)