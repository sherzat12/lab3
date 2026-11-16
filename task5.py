# Задача 5. Произведение членов последовательности, кратных p
n, p = map(int, input().split())
a = list(map(int, input().split()))
r = 1
for x in a:
    if x % p == 0:
        r *= x
print(r)
