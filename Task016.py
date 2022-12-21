

import random


def NumEnter(n):
    while True:
        try:
            if int(n) > 0:
                break
            if int(n) <= 0:
                n = int(input('Введите целое число от 1 и выше: '))
        except:
            n = int(input('Ввод не верный, повторите ввод: '))
    return int(n)


def Array(k):
    array = []
    i = 0
    for i in range(0, k):
        array.append(random.randint(1, k // 2))
    return array


def FindNumberX(array, m):
    count = 0
    for i in range(len(array)):
        if m == array[i]:
            count += 1
    return count

number = NumEnter(input('Введите целое положительное число от 1-го: '))
arrayFyst = Array(int(number))
print(arrayFyst)

numberX = NumEnter(input('Введите целое положительное \
число от 1-го \n чтобы посчитать сколько раз оно повтаряется: '))

if FindNumberX(arrayFyst, int(numberX)) == 0:
    print(f'Числа {numberX} нет в массиве')
else:
    print(f'число {numberX} повторяется {FindNumberX(arrayFyst, int(numberX))}')

