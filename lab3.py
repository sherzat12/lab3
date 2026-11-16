"""
Лабораторная работа 3. Сочетание цикла и разветвления.
Задачи: 1а, 1б, 3а, 3б, 4, 5.
Числа вводятся в одну строку через пробел.
"""
import sys


def task1a():
    """1а. Количество членов, являющихся нечётными числами."""
    n = int(input("n = "))
    a = list(map(int, input("a1..an: ").split()))[:n]
    k = 0
    for x in a:
        if x % 2 != 0:
            k += 1
    print("Количество нечётных:", k)


def task1b():
    """1б. Количество членов, кратных 3 и не кратных 5."""
    n = int(input("n = "))
    a = list(map(int, input("a1..an: ").split()))[:n]
    k = 0
    for x in a:
        if x % 3 == 0 and x % 5 != 0:
            k += 1
    print("Количество кратных 3 и не кратных 5:", k)


def task3a():
    """3а. Сумма чисел (из 50), кратных 5."""
    a = list(map(int, input("a1..a50: ").split()))[:50]
    s = 0
    for x in a:
        if x % 5 == 0:
            s += x
    print("Сумма кратных 5:", s)


def task3b():
    """3б. Сумма нечётных и отрицательных чисел (из 50)."""
    a = list(map(int, input("a1..a50: ").split()))[:50]
    s = 0
    for x in a:
        if x % 2 != 0 and x < 0:
            s += x
    print("Сумма нечётных и отрицательных:", s)


def task4():
    """4. Количество и сумма членов, которые делятся на 5 и не делятся на 7."""
    n = int(input("n = "))
    a = list(map(int, input("a1..an: ").split()))[:n]
    k = 0
    s = 0
    for x in a:
        if x % 5 == 0 and x % 7 != 0:
            k += 1
            s += x
    print("Количество:", k)
    print("Сумма:", s)


def task5():
    """5. Произведение членов, кратных p."""
    n, p = map(int, input("n p = ").split())
    a = list(map(int, input("a1..an: ").split()))[:n]
    r = 1
    for x in a:
        if x % p == 0:
            r *= x
    print("Произведение кратных p:", r)


TASKS = {
    "1а": task1a,
    "1б": task1b,
    "3а": task3a,
    "3б": task3b,
    "4": task4,
    "5": task5,
}


def main():
    while True:
        print("\nВыберите задачу: " + ", ".join(TASKS) + " (0 - выход)")
        choice = input("> ").strip().lower()
        if choice == "0":
            sys.exit(0)
        if choice in TASKS:
            TASKS[choice]()
        else:
            print("Нет такой задачи")


if __name__ == "__main__":
    main()
