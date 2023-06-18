n = int(input("Введите количество элементов первого множества: "))
list_1 = [int (i) for i in input("Введите через пробел элементы первого множества: ").split()][:n]
m = int(input("Введите количество элементов второго множества: "))
list_2 = [int (j) for j in input("Введите через пробел элементы второго множества: ").split()][:m]
list_3 = []
for i in list_1:
    if i not in list_2:
        list_3.append(i)
print(*(list_3))
