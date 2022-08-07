#  Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#  Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = list(map(int, input('Enter your space-separated numbers:\n').split()))
summ = sum([elem for i, elem in enumerate(my_list) if i % 2 != 0])
print('The sum of items with odd indexes:\n', summ)
