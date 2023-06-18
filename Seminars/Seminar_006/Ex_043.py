n = int(input("Введите количество элементов первого множества: "))
list_1 = [int (i) for i in input("Введите через пробел элементы первого множества: ").split()][:n]
result = {}

for i in list_1:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
 
print(sum([i//2 for i in result.values()]))