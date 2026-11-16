# лаб 3 - цикл и ветвление

# 1а - сколько нечетных
print("задача 1а")
n = int(input("n = "))
k = 0
for i in range(n):
    a = int(input())
    if a % 2 == 1:
        k = k + 1
print("нечетных:", k)

# 1б - кратных 3 и не кратных 5
print("задача 1б")
n = int(input("n = "))
k = 0
for i in range(n):
    a = int(input())
    if a % 3 == 0 and a % 5 != 0:
        k = k + 1
print("количество:", k)

# 3а - сумма кратных 5 (50 чисел)
print("задача 3а")
s = 0
for i in range(50):
    a = int(input())
    if a % 5 == 0:
        s = s + a
print("сумма:", s)

# 3б - сумма нечетных и отрицательных (50 чисел)
print("задача 3б")
s = 0
for i in range(50):
    a = int(input())
    if a % 2 != 0 and a < 0:
        s = s + a
print("сумма:", s)

# 4 - количество и сумма тех что делятся на 5 и не делятся на 7
print("задача 4")
n = int(input("n = "))
k = 0
s = 0
for i in range(n):
    a = int(input())
    if a % 5 == 0 and a % 7 != 0:
        k = k + 1
        s = s + a
print("количество:", k)
print("сумма:", s)

# 5 - произведение тех что кратны p
print("задача 5")
n = int(input("n = "))
p = int(input("p = "))
pr = 1
for i in range(n):
    a = int(input())
    if a % p == 0:
        pr = pr * a
print("произведение:", pr)
