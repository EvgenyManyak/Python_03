# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся через пробел в одной строкой.

from random import randint

n = int(input('Введите число: --> '))
numbers = []
for i in range(n):
    numbers.append(randint (-n, n))
print(numbers)

x = int(input('Индекс первого элемента: --> '))
y = int(input('Индекс второго элемента: --> '))

for i in range(len(numbers)):
    res_mult = numbers[x - 1] * numbers[y - 1]
print(res_mult)