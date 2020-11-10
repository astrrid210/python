# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

full_sum = 0
stop_signal = False
while True:
    splitted_data = input("enter numbers: ").split(" ")
    new_sum = 0
    for element in splitted_data:
        if element == "!":
            stop_signal = True
            break
        new_sum += float(element)
    full_sum += new_sum
    print(f"full sum is {full_sum}, recent sum is {new_sum}")
    if stop_signal:
        break
