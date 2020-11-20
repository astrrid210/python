# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('salaries.txt') as f:
    salaries = []
    lines = f.readlines()
    for new_line in lines:
        name, salary = new_line.split(' - ')
        salaries.append(float(salary))
        if float(salary) < 20000:
            print(new_line, end='')
    print('\nAverage salary:', sum(salaries) / len(salaries))
