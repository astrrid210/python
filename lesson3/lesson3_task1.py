# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def division(dividend, divisor):
    if divisor == 0:
        return None
    return dividend / divisor


dividend = int(input("enter dividend.. "))
divisor = int(input("enter divisor.. "))

print("result of division is ", division(dividend, divisor))
