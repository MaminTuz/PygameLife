def cym(m, n):
    p = m + n
    return p
def vich(m, n):
    p = m - n
    return p
def proz(m, n):
    p = m * n
    return p
def deln(m, n):
    p = m / n
    return p
def ost(m, n):
    p = m % n
    return p
def proc(m, n):
    p = m * 100 / n
    return p
def fact(m):
    if m == 0:
        return 1
    elif m < 0:
        return 'НЕЗЯ'
    else:
        return m * fact(m - 1)
def nod(m, n):
    if n == 0:
        return m
    else:
        return nod(n, m % n)
def nok(m, n):
    p = proz(m,n) * nod(m,n)
    return p
def prost(n):
    i = 2
    while n != i - 1:
        if n % i == 0:
            if n != i:
                p = 'не простое'
                i = n
            elif n == i:
                p = 'простое'
                i += 1
        else:
            i += 1
    return p
i = 1
while i == 1:
    a = int(input('Введите первое число '))
    b = int(input('Введите второе число '))
    d = 0
    c = int(input("""'Выберите действие 1 - сложение'
'2 - вычитание'
'3 - умножение 4 - деление 5 - нахождение остатка от числа 6 - процент от числа 7-факториал 8-наибольший общий делитель 9-наименьшее общее кратное 10- является ли первое число простым '"""))
    if c == 1:
        d = cym(a, b)
    elif c == 2:
        d = vich(a, b)
    elif c == 3:
        d = proz(a, b)
    elif c == 7:
        d = fact(a)
    else:
        try:
            if c == 4:
                d = deln(a, b)
            elif c == 5:
                d = ost(a, b)
            elif c == 6:
                d = proc(a, b)
            elif c == 8:
                d = nod(a, b)
            elif c == 9:
                d = nok(a, b)
            elif c == 10:
                d = prost(a)
            else:
                print('Такой функции нет')
        except:
            d = 'error'
    print(f'Ответ: {d}')
    i = int(input('Хотите завершить операцию? ДА-2 НЕТ-1 '))

