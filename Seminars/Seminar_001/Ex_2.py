# Найдите сумму цирф трехзначного числа

n = int(input ("Введите трехзначноие число: "))

m = n // 100 + n % 100 // 10 + n % 10
print(m)