import random


def cym(mas, m):
    p = 0
    for i in range(0, m):
        p+=mas[i]
    return p

def sred(mas, n):
    p = 0
    for i in range(0, n):
        p = (p + mas[i]) / i + 1
    return p

def max(mas, n):
    p=0
    for i in range(0, n):
        if p < mas[i]:
            p = mas[i]
    return p

def min(mas, n):
    p = mas[0]
    for i in range(0, n):
        if p > mas[i]:
            p = mas[i]
    return p

def sorpV(mas, n):
    for i in range (0, n):
        for j in range (0, n-1):
            if mas[j] < mas[j+1]:
                c = mas[j]
                mas[j] = mas[j + 1]
                mas[j + 1]= c
    return mas

def sorpU(mas, n):
    for i in range (0, n):
        for j in range (0, n-1):
            if mas[j] > mas[j+1]:
                c = mas[j]
                mas[j]=mas[j+1]
                mas[j+1]=c
    return mas

def otkl(mas, n, h, j):
    p = 0
    mas2 = []
    for i in range(0, n):
        m = random.randint(h, j)
        mas2.append(m)
    for i in range (0, n):
        t = abs(mas[i]-mas2[i])/mas[i]
        p += t
    p = p/(n+1)
    return p
k = 1
while k == 1:
    a = int(input('Введите размер массива '))
    b = int(input('Введите число которе будет началом диапазона '))
    g = int(input('Введите число которе будет концом диапазона '))
    d = 0
    l = 0
    c = int(input("""'Выберите действие 1 - сумма чисел массива'
'2 - Нахождение среднего 3 - нахождение максимального элема'
'4 - нахождение минимального элема 5 - сортировка по возрастанию'
'6 - сортировка по убыванию 7 - отклонения '"""))
    mas1 = []
    for i in range(0, a):
        m = random.randint(b, g)
        mas1.append(m)
    print(mas1)
    if c == 1:
        d = cym(mas1, a)
    elif c == 2:
        d = sred(mas1, d)
    elif c == 3:
        d = max(mas1, a)
    elif c == 4:
        d= min(mas1, a)
    elif c == 5:
        d = sorpV(mas1, a)
    elif c == 6:
        d = sorpU(mas1, a)
    elif c == 7:
        d = otkl(mas1, a, b, g)
    print(f'Ответ: {d}')
    k = int(input('Хотите завершить операцию? ДА-2 НЕТ-1 '))

