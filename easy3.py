# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
#
#
#
#
# name = input('введите имя')
# age = input('введите возраст')
# city = input('Введите город проживания')
# #
# print(name, age, 'год(а)', 'проживает в городе ', city)
#





# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них



# a = int(input('введите число 1'))
# b = int(input('введите число 2'))
# c = int(input('введите число 3'))
#
# def max_num(*args):
#     return max(*args)
# print (max_num(a, b, c))

# for max in data_1




# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def input_args(*args):
    arg_list = []
    for x in args:
        arg_list.append(x)
        arg_list.sort(key=len)
    return arg_list[-1]


print(input_args('8980', '123heehe', 'ad', 'f12oieo', 'weqwe', 'iwheiudhw'))