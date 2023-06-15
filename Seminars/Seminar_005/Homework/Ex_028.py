# Вводится десятичное число. 
# Реализовать алгоритм его перевода в двоичную систему счисления через рекурсию. 

def binary(n):
    if n == 0 or n == 1:
        return f'{n}'
    return binary(n // 2) + f'{n % 2}'

n = int(input())
print(binary(n))
