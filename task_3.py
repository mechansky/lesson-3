def my_func(a, b, c):
    return f'результат: {(float((a + b + c) - min(a, b, c)))}'


a = float(input('введите первое число: '))
b = float(input('введите второе число: '))
c = float(input('введите третье число: '))

print(my_func(a, b, c))

