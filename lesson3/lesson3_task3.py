# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a <= b and a <= c:
        return b + c
    if b <= a and b <= c:
        return a + c
    return a + b


val1 = float(input("enter first value.. "))
val2 = float(input("enter second value.. "))
val3 = float(input("enter third value.. "))

print("max sum is", my_func(val1, val2, val3))
