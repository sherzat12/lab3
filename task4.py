# Задача 4. Количество и сумма членов, которые делятся на 5 и не делятся на 7
n = int(input())
a = list(map(int, input().split()))
k = 0
s = 0
for x in a:
    if x % 5 == 0 and x % 7 != 0:
        k += 1
        s += x
print(k, s)
