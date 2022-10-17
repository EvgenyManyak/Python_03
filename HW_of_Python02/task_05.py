# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся через пробел в одной строкой.

numbers = []
n = int(input('Введите число: --> '))
numbers = [i for i in range(-n, n)]
print(f'Список элементов: {numbers}')
index_num = input('--> ').split()
res_mult = 1
for item in index_num:
    res_mult *= numbers[int(item)]
print(res_mult)