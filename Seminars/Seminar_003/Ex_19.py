list_1 = [int(i) for i in input().split()]
step = int(input("введите количество сдвигов: "))
result_list = [list_1[i-step] for i in range(len(list_1))]
print(result_list)

