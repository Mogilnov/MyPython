def revert(n):
    if n == 0:
        return ""
    k = int(input())
    return revert(n-1) + f" {k}"

n = int(input())
print(revert(n))
