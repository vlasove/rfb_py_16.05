# Решение задачи O
n_tasks = int(input())
tasks = []

for _ in range(n_tasks):
    tasks.append(input())

n_tasks_to_build = int(input())
for _ in range(n_tasks_to_build):
    task_id = int(input())
    print(tasks[task_id - 1])