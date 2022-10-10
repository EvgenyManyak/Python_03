# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from itertools import count


def my_list(list1):
    count = 0
    for i in range(len(list1)):
        if i % 2 == 1:
            count += list1[i]
    print(f"Сумма нечетных чисел: {count}")
list1 = [3, 5, 6, 7, 11]
my_list(list1)
list1 = list(map(int, input("Введите числа через пробел:\n").split()))
my_list(list1)