#  Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = list(map(int, input('Enter your space-separated numbers:\n').split()))
my_prods = [(lst[i] * lst[len(lst)-1-i]) for i in range(len(lst)) if lst[i] <= lst[len(lst)-1-i]]
print('The produсts of pairs of numbers:\n', my_prods)
