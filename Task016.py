# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число,
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 3

# 1 2 3 4 5
# Вывод: 1

import random


def NumEnter(n, l):
    while True:
        try:
            if int(n) > 0 and int(l) >= 0:
                break
            if int(n) < 1:
                n = int(input('Введите целое число от 1 и выше: '))
            if int(l) < 0:
                l = int(input('Введите целое число от 0 и выше: '))
        except:
            n = int(input('Ввод массива не верный, повторите ввод: '))
            l = int(input('Ввод не верный, повторите ввод: '))
    return int(n), int(l)


def Array(k):
    array = []
    i = 0
    for i in range(0, k):
        array.append(random.randint(0, k // 2))
    return array


def FindNumberX(array, m):
    count = 0
    for i in range(0, len(array)):
        if m == array[i]:
            count += 1
    return count


number = NumEnter(input('Введите длинну массива: '), 0)[0]
arrayFyst = Array(int(number))
print(arrayFyst)

numberX = NumEnter(1, input('Введите целое положительное \
число от 1-го \n чтобы посчитать сколько раз оно повтаряется: '))[1]
if FindNumberX(arrayFyst, int(numberX)) == 0:
    print(f'Числа {numberX} нет в массиве')
else:
    print(f'число {numberX} повторяется {FindNumberX(arrayFyst, int(numberX))}')
