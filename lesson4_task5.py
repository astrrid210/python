# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import functools


def mul_list(accumulation, element):
    return accumulation * element


generated_list = [x for x in range(100, 1001, 2)]
multiplication_result = functools.reduce(mul_list, generated_list)
print(multiplication_result)
