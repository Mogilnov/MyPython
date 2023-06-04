# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X 

N = abs(int(input('Введите количество элементов списка А: ')))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('Введено неверное количество элементов')
else:
    X = int(input('Введите число X: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(A_num[index])