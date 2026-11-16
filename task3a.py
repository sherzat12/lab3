# Задача 3а. Сумма чисел последовательности (50 чисел), кратных 5
a = list(map(int, input().split()))  # 50 чисел
s = 0
for x in a:
    if x % 5 == 0:
        s += x
print(s)
