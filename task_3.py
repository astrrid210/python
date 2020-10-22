# task 3
# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число n: '))
nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))
total_sum = n + nn + nnn
print('Вы ввели число n =', n)
print('Считаем ', n, '+', nn, '+', nnn, '=', total_sum, '.')



