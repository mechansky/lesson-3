def my_func():
    result = 0
    while True:
        numbers = []
        user_input = input('функция "сумма чисел". для выхода введите "q"\nвведите числа через пробел: ').split()
        list_to_float(user_input, numbers)
        if user_input[-1] == 'q' or user_input[-1] == 'Q':
            print(f'подсчет окончен! конечный результат: {result + sum(numbers[0:-1])}')
            break
        else:
            result += sum(numbers)
            print(f' результат: {result}')


def list_to_float(basic_list, result_list):  # создал отдельную функцию для перевода элементов списка в числа
    for element in basic_list:
        try:
            result_list.append(float(element))
        except Exception:
            result_list.append(element)
    return result_list


my_func()
