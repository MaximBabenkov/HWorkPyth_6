# Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число. 

list_in = input('Enter your space-separated numbers:\n').split()
numb = input('Enter your number:\n')
list_out = list(filter(lambda x: numb in x, list_in))
# или list_out = [i for i in list_in if numb in i]
if list_out != []:
    print('Your number is contained in this list')
else:
    print('Your number is not contained in this list')
