# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

element = input('Введите значение элемента. Для прекращения ввода элементов введите no: ')
new_list = [element]
while element != 'no':
    element = input('Введите значение элемента. Для прекращения ввода элементов введите no: ')
    if element != 'no':
        new_list.append(element)
quantity = len(new_list)
for el in range(1, quantity, 2):
    new_list[el - 1], new_list[el] = new_list[el], new_list[el - 1]
print(new_list)