n = int(input("Введите количество элементов первого множества: "))
list_1 = [int (i) for i in input("Введите через пробел элементы первого множества: ").split()][:n]
count = 0

for i in range(1, n-1):
    if list_1[i]>list_1[i-1] and list_1[i+1]:
        count += 1
print(count)
