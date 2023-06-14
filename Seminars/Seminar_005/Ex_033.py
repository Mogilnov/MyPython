list_1 = [int(i) for i in input("Введите через пробел оценки Василия: ").split()]
n = max(list_1)
m = min(list_1)
for i in range(len(list_1)):
    if list_1[i] == n:
        list_1[i] = m
print(*list_1)