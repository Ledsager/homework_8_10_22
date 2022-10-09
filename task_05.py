# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from math import sqrt
from random import randint

# Ввод координат точки (через пробел)


def Coordinate():
    coord = []
    coord=[int(i) for i in input().split()]
    # генерация координат точек в определенном диапазоне
    # coord = []
    # i=0
    # while (i < 2):
    #     coord.append(randint(0, 10))  
    #     i = i+1
    return coord

# Функция расчета отрезка между 2я точками


def DistancePoints(point1, point2):
    dist = 0
    i = 0
    for i in range(len(point1)):
        dist = dist + (point1[i]-point2[i])*(point1[i]-point2[i])
        print(f"разница между координатами: {(point1[i]-point2[i])}")
        print(f"квадрат разницы  координат: {(point1[i]-point2[i])*(point1[i]-point2[i])}")
    dist = round(sqrt(dist), 4)
    return dist

print('Введите значение координат первой точки (через пробел):')
a = Coordinate()
print('Введите значение координат второй точки (через пробел):')
b = Coordinate()
if (len(a)==2) and (len(b)==2):
    c = DistancePoints(a, b)
    print(f'координата точки А {a}')
    print(f'координата точки В {b}')
    print(f'расстояние между точками = {c}')
else:
    print('Введены не верные значения координат')
