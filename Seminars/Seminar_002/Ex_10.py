# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монет: "))
count = 0
for i in range(n):
    x = int(input("Орёл(0) или решка (1)"))
    if x == 1:
       count += 1
if count < n/2:
    print(count)
else:
    print(n-count)

    

