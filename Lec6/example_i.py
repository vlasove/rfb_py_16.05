# Решение задачи E

general = set()
n_days = int(input()) # Количество дней в семестре

for i in range(n_days):
    n_students = int(input()) # Количество студентов, пришедших в n день
    students_set = set() # Множество фамилий студентов пришедших в n день
    for _ in range(n_students):
        students_set.add(input())
    
    if i == 0: # Это первый день семестра
        general = general.union(students_set)
    else:
        general = general.intersection(students_set)

print(len(general))