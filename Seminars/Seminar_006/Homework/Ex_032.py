# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [int(i) for i in input("Введите через пробел элементы списка: ").split()]
min_item = int(input())
max_item = int(input())
for i in range(len(list_1)):
    if min_item <= list_1[i] <= max_item:
        print(i)
 


