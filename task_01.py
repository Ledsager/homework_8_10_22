# Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Введите день недели(1..7)'))

if (a < 1) or (a > 7):
    print(f'{a} - такого дня недели нет')
elif a == 6 or a == 7:
    print(f'{a} - это выходной день')
else:
    print(f'{a} - это рабочий день')
