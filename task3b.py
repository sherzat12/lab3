# Задача 3б. Сумма нечётных и отрицательных чисел (50 чисел)
a = list(map(int, input().split()))  # 50 чисел
s = 0
for x in a:
    if x % 2 != 0 and x < 0:
        s += x
print(s)
