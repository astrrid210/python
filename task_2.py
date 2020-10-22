# task 2
# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


seconds = int(input('Введите время в секундах: '))
seconds_in_minute = 60
minutes_in_hour = 60
minutes = seconds // seconds_in_minute
remainder_from_minutes = seconds % seconds_in_minute
hours = minutes // minutes_in_hour
remainder_from_hours = minutes % minutes_in_hour

if seconds < 360000:
    print(' {0} : {1} : {2}'.format("%.2d" % hours, "%.2d" % remainder_from_hours, "%.2d" % remainder_from_minutes))
else:
    print('Ошибка. Попробуйте ввести время менее 360000 секунд')














