# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
list_1 = [int (i) for i in input("Введите через пробел элементы первого множества: ").split()]
while len(list_1) != n:
    print ("введено неверное количество элементов")
    list_1 = [int (i) for i in input("Введите через пробел элементы первого множества: ").split()]
list_2 = [int (j) for j in input("Введите через пробел элементы второго множества: ").split()]
while len(list_2) != n:
    print ("введено неверное количество элементов")
    list_2 = [int (i) for i in input("Введите через пробел элементы второго множества: ").split()]
list_3 = []

for i in list_1:
    for j in list_2:
        if i==j:
            list_3.append(i)
print(*set(sorted(list_3)))