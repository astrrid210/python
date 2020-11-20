# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('numbers.txt', 'w') as f:
    nums = input('Please enter integers separated with spaces: ')
    f.write('Your data: ' + nums + '\n')
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    f.write('Total: ' + str(sum_nums))
    print('Sum:', sum_nums)
print('ur data is recorded')
