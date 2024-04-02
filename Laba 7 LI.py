import random


class Animals:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dir):
        if dir == 0:
            self.x += 1
        elif dir == 1:
            self.y += 1
        elif dir == 2:
            self.x -= 1
        elif dir == 3:
            self.y -= 1

class Wolfs(Animals):
    def __init__(self, x, y):
        self.attack = 100
        self.health = 9999999
        self.pos = Animals(x, y)

    def attack(self, sheeps):
        sheeps.take_damage(self.attack)

class Sheeps:
    def __init__(self, x, y):
        self.attack = 0
        self.health = 1
        self.pos = Animals(x, y)
        self.is_alive = True

    def be_eaten(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False

def process_eat(x, y, field, sheep, sheeps):
    if not is_crossed_borders(x, y, field):
        if field[y][x] == "s":
            for sheep in sheeps:
                if sheep.x == x and sheep.y == y:
                    sheep.eat(sheep)
                    break

def is_crossed_borders(x, y, field):
    return x < 0 or y < 0 or y >= len(field) or x >= len(field[0])


def render(field):
    for y in range(len(field)):
        for x in range(len(field[0])):
            print(field[y][x], end='')
        print()
    print('--------------------------------------')


def main():
    size = int(input("Введите размер поля: "))
    sheeps_number = int(input("Сколько будет овец: "))
    wolfs_number = int(input("Сколько будет Волков: "))
    sheeps_count = []
    wolfs_count = []
    field = [[' '] * size for i in range(size)]

    for i in range(sheeps_number):
        x = random.randint(0, len(field[0]) - 1)
        y = random.randint(0, len(field) - 1)
        sheep = Sheeps(x, y)
        sheeps_count.append(sheep)

    for i in range(wolfs_number):
        x = random.randint(0, len(field[0]) - 1)
        y = random.randint(0, len(field) - 1)
        wolf = Wolfs(x, y)
        wolfs_count.append(wolf)

    for sheep in sheeps_count:
        field[sheeps_count.pos.y][sheeps_count.pos.x] = 's'

    for wolf in wolfs_count:
        field[wolfs_count.pos.y][wolfs_count.pos.x] = 'W'

    while sheeps_number > 0:
        for wolf in wolfs_count:
            for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x = wolf.pos.x + i[0]
                y = wolf.pos.y + i[1]
                process_eat(x, y, field, sheep, sheeps_count)


            field[wolfs_count.pos.y][wolfs_count.pos.x] = ' '
            old_x = wolfs_count.pos.x
            old_y = wolfs_count.pos.y
            direction = random.randint(0, 3)
            wolf.move(direction)


