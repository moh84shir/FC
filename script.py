import os
RANGE_NUM = int(input('Number of dirs : '))
NAME_RANGE = input('Name of dirs : ')
DIR_NUM = RANGE_NUM + 1
DIR_NAMES = list(range(0, DIR_NUM))
DIR_NAMES.pop(0)

for DIR_NAME in DIR_NAMES:
    os.system(f'mkdir {NAME_RANGE}_{DIR_NAME}')