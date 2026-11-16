# Задача 1б. Количество членов, кратных 3 и не кратных 5
n = int(input())
a = list(map(int, input().split()))
k = 0
for x in a:
    if x % 3 == 0 and x % 5 != 0:
        k += 1
print(k)
