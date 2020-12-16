def my_division(a, b):
    try:
        result = a / b
        return f'результат: {round(result, 2)}'
    except ZeroDivisionError as error:
        return 'на ноль делить нельзя!'


a = (input('введите число, которое мы будем делить: '))
b = (input(f'введите число, на которое мы будем делить число {a}: '))
print(my_division(float(a), float(b)))
