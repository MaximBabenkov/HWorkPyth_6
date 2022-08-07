#  Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов.

#     Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = list(map(float, input('Enter your space-separated numbers:\n').split()))
fract_parts = [lst[i] - int(lst[i]) for i in range(len(lst)) if lst[i] > 0]
res = max(fract_parts) - min(fract_parts)
print('The diffirence:', round(res, 2))   
