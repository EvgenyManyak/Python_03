# Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.

def factorial (number, count = 1):
    for i in range(1, number + 1):
        count *= i
    return count
n = int(input('Введите число: --> '))
print(factorial(5))