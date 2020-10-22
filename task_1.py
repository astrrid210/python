# task 1

# 1. Поработайте с переменными,
# создайте несколько,
# выведите на экран,
# запросите у пользователя несколько чисел и строк
# и сохраните в переменные,
# выведите на экран.

name = input('Ваше имя? ')
print('Привет, %s!' % name)
birthday_year = int(input('В каком году вы родились?'))
birthday_date = int(input('Какого числа вы родились?'))
birthday_month = input('В каком месяце вы родились?')
current_year = int(input('Какой сейчас год? '))
current_age = current_year - birthday_year
print('Меня зовут ', name)
print('Моя дата рождения: ', birthday_date, birthday_month, birthday_year, )
print('Мой возраст', current_age, 'лет')


