import timeit ##Библиотека для бентчмаркинга

mysetupToMySqrt = "from math import sqrt"  

mycodeToMysqrt = '''
def my_sqrt(k, real_sqrt): ##Функция, вычмсляющее значение корня с заданной точностью относительно реального значения
    a = 2                  ##Храним два предыдущих значения из рекурсии
    b = 2
    while (abs(b / a - 1 - real_sqrt) > 0.001): ##Цикл работает пока не достигнем определённой точности (0.01)
        tmp = a
        a = b
        b = 2 * a +  (k - 1) * tmp
    return b / a - 1
x = my_sqrt(100, sqrt(100))

'''
mysetupToRealSqrt = "from math import sqrt"
mycodeToRealSqrt = '''
x = sqrt(100)  ##Просто вычисляем корень
'''

print ("My_sqrt worked ", timeit.timeit(setup = mysetupToMySqrt,
					stmt = mycodeToMysqrt,
					number = 100000) - timeit.timeit(setup = mysetupToRealSqrt,
					stmt = mycodeToRealSqrt,
					number = 100000))                     ##Время работы моего корня = время работы первой функции - время раблты второй (реального корня)
print("Base sqrt worked ", timeit.timeit(setup = mysetupToRealSqrt,
					stmt = mycodeToRealSqrt,
					number = 100000))                     ##время работы реального корня, который вычисляется во второй функции
