# task 4
# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# Решение №1 с помощью while:
number = int(input('Введите целое положительное число: '))
big_figure = number % 10
number = number // 10
while number > 0:
    if number % 10 > big_figure:
        big_figure = number % 10
    number = number // 10
print('Самая большая цифра в числе: ', big_figure)

# Решение №2 с помощью for in:
# number = input('Введите целое положительное число: ')
# biggest_figure = max([int(i) for i in str(number)])
# print('Самая большая цифра в числе: ', biggest_figure)