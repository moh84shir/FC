import os
RANGE_NUM = int(input('Count of dirs : '))
NAME_DIR = input('Name of dirs : ')
DIR_COUNT = RANGE_NUM + 1
DIR_NAMES = list(range(0, DIR_COUNT))
DIR_NAMES.pop(0)

for DIR_NAME in DIR_NAMES:
    os.system(f'mkdir {NAME_DIR}_{DIR_NAME}')
