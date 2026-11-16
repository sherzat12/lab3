# Задача 1а. Количество членов последовательности, являющихся нечётными числами
n = int(input())
a = list(map(int, input().split()))
k = 0
for x in a:
    if x % 2 != 0:
        k += 1
print(k)
