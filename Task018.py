# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, 
# выведите наименьший.

# Ввод: 5
# Ввод: 6
# 1 2 0 4 7
# Вывод: 7

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
    i = 0
    n = l = m
    if m in array:
        print(f'Число {m} равно чеслу из массив')
    else:
        while True:
            l -= 1
            n += 1
            if l in array and n in array:
                print(f'Числа {l} и {n}, самые близкие числа из массива к числу {m}.')
                break
            if l in array:
                print(
                    f'Число {l}, самoе близкое близкое число из массива кчислу {m}.')
                break
            if n in array:
                print(
                    f'Число {n}, самoе близкое близкое число из массива кчислу {m}.')
                break







numberN = NumEnter(input('Введите длинну массива: '), 0)[0]
arrayFyst = Array(int(numberN))
print(arrayFyst)

numberX = NumEnter(1, input('Введите целое положительное \
число от 0 \n чтобы найти это значение в массиве или близкое к нему: '))[1]


FindNumberX(arrayFyst, numberX)

# еле поймал на оба числа
# Введите длинну массива: 50
# [17, 24, 16, 23, 5, 6, 13, 22, 1, 9, 14, 4, 11, 10, 9, 15, 20, 3, 3, 25, 23, 5, 20, 5, 0, 23, 6, 24, 17, 11, 6, 23, 14, 11,
#  4, 11, 0, 6, 8, 12, 23, 8, 14, 6, 3, 18, 5, 1, 5, 4]
# Введите целое положительное число от 0
# чтобы найти это значение в массиве или близкое к нему: 2
# Числа 1 и 3, самые близкие числа из массива к числу 2.