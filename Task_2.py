#  Напишите программу, которая определит позицию второго вхождения строки
# в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

my_list = input('Enter your space-separated strings:\n').split()
my_string = input('Enter your string to find:\n')
indexes = [i for i, name in enumerate(my_list) if name == my_string]
if len(indexes) >= 2:
    my_index = indexes[1]
    print('Your index of the second entry:', my_index)
else:
    print('There is no second entry')