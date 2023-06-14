def exp(a, b):
    if b == 0:
        return 1
    return exp(a, b - 1) * a

a = int(input())
b = int(input())
print(exp(a, b))
