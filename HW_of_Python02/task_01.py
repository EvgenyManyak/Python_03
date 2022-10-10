# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from itertools import count


def digit_sum(n):
    num_lst = list(str(n))
    count = 0
    for i in range(len(num_lst)):
        count += int(num_lst[i])
    return count
n = int(input('Введите число: --> '))
print(digit_sum(n))