# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

print(sys.argv)
if len(sys.argv) == 4:
    time = int(sys.argv[1])
    rate = int(sys.argv[2])
    bonus = int(sys.argv[3])
    print(f"time: {time}, rate: {rate}, bonus: {bonus}, total to pay: ", rate*time+bonus)
else:
    print("no correct args provided to script, try launch with 'time rate bonus' args")
