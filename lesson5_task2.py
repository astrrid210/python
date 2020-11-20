# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('test.txt') as f:
    lines = f.readlines()
    print('quantity of strings:', len(lines))
    for num_line, line in enumerate(lines, start=1):
        print('string № {} contains - {} word(s)'.format(num_line, len(line.split())))
