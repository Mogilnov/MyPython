list_1 = [0, -1, 5, 2, 3]
count = 0
for i in range(len(list_1)-1):
    if list_1[i] < list_1[i+1]:
        count = count + 1
print(count)