# Задайте список из n чисел последовательности (1 + 1 \ n)^n и выведите на экран их сумму.

from itertools import count


n = int(input("Введите число n: "))
count = 0
for i in range(1, n + 1):
    count += (1 + 1 / i)**i
    print(round(count, 2))