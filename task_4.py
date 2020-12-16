def my_func(x, y):
    return f'результат: {x ** y}'

print('Способ №1 (через **): ')
x = float(input('введите целое положительное число: '))
y = float(input('введите целое отрицательное число: '))
print(my_func(x, y))


def my_func2(x, y):
    result = 1
    i = 0
    y = abs(y)
    while i != y:
        result *= x
        i += 1
    return f' результат: {1 / result}'

print('Способ №2 (через цикл): ')
x = float(input('введите целое положительное число: '))
y = float(input('введите целое отрицательное число: '))
print(my_func2(x, y))




