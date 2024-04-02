import random


def place_ships(field2):
    ships = 0
    while ships <= 5:
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        while field2[x][y] == 1:
            x = random.randint(0, 4)
            y = random.randint(0, 4)
        field2[x][y] = 1
        ships += 1
    return field2


def check_field(field1):
    for y in range(0, len(field1)):
        for x in range(0, len(field1[0])):
            if field1[y][x] == 0 or field1[y][x] == 1:
                print('_', end='')
            elif field1[y][x] == 2:
                print('X', end='')
            elif field1[y][x] == 3:
                print('0', end='')
        print()


def main():
    ships = 5
    field = [[0]*5 for i in range(5)]
    check_field(field)
    while ships > 0:
        x = int(input('Координата выстрела x '))
        y = int(input('Координата выстрела y '))
        while x >= 5 or y >= 5 or x < 0 or y < 0:
            print('кординаты от 0 до 4 должны быть')
            x = int(input('Координата выстрела x '))
            y = int(input('Координата выстрела y '))
        if field[x][y] == 1:
            field[x][y] = 2
            place_ships(field)
            ships -= 1
        else:
            print('косой')
            field[x][y] = 3
            place_ships(field)
    print('VICTORY')


main()
