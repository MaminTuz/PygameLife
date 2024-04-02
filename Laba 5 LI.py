import random
num_players = int(input('Введите количество игроков: '))
size = int(input('Размер поля: '))
field = [[0] * size for i in range(size)]
characters = []
enemy = []
enemy_x = []
enemy_y = []
ty = 0
enemy_fight_y = [-5] * num_players
enemy_fight_x = [-5] * num_players
tech_list = ['type', 'number', 'name', 'health', 'attack', 'defence']
len_tech_list = len(tech_list)
x = random.randint(0, size - 1)
y = random.randint(0, size - 1)
hp = 0
zas = 0
at = 0
for l in range(num_players):
    name = input('Введите имя игрока: ')
    char = [['Боец', l+1, name, 100, 10, 3]]
    characters.append(char)
    for a in char:
        for i in range(len_tech_list):
            print(f"""{tech_list[i]} {a[i]}""")
    if l == 0:
        field[y][x] = 1
        player = characters[l]

    else:
        enemy.append(characters[l])
        proverka = 0
        while proverka == 0:
            ey = random.randint(0, size - 1)
            ex = random.randint(0, size - 1)
            if field[ey][ex] == 0 and proverka == 0:
                field[ey][ex] = 2
                enemy_y.append(ey)
                enemy_x.append(ex)
                proverka += 1


print(characters)
while len(characters) > 1:
    for lp in range(100):
        print()
    for a in range(0, len(field)):
        for b in range(0, len(field[0])):
            if field[a][b] == 0:
                print('+', end='')
            elif field[a][b] == 1:
                print('P', end='')
            elif field[a][b] == 2:
                print('E', end='')
        print()
    if ty == 1:
        print('Ваши характеристики возросли')
        ty = 0
    napr = input('Введите направление w a s d: ')

    dx = x
    dy = y
    if napr == 'w':
        dy -= 1
    elif napr == 'a':
        dx -= 1
    elif napr == 'd':
        dx += 1
    elif napr == 's':
        dy += 1
    if 0 <= dx < size and 0 <= dy < size and field[dy][dx] == 0:
        field[dy][dx] = 1
        field[y][x] = 0
        x = dx
        y = dy
    else:
        print()

    for i in range(len(characters)):
        if i < len(enemy):
            edy = enemy_y[i]
            edx = enemy_x[i]
            m = random.choice([1,2])
            if m == 1:
                edx += random.randint(-1,1)
            if m == 2:
                edy += random.randint(-1, 1)
            if 0 <= edx < size and 0 <= edy < size and field[edy][edx] == 0:
                field[edy][edx] = 2
                field[enemy_y[i]][enemy_x[i]] = 0
                if dx == enemy_x[i] and dy == enemy_y[i]:
                    field[dy][dx] = 1
                    field[y][x] = 0
                    y = dy
                    x = dx
                enemy_y[i] = edy
                enemy_x[i] = edx
            else:
                if dx == enemy_x[i] and dy == enemy_y[i]:
                    edx = dx
                    edy = dy
                enemy_fight_x[i] = edx
                enemy_fight_y[i] = edy

                print()

    player_healt = player[0][3] + hp
    player_defance = player[0][5] + zas
    player_attack = player[0][4] + at
    enemy_healt = enemy[0][0][3]
    enemy_defance = enemy[0][0][5]
    enemy_attack = enemy[0][0][4]
    print('Здоровье противника:', enemy_healt)
    print('Ваше здоровье', player_healt)

    l = len(characters)
    p = len(enemy_fight_x)

    for t in range(p):
        if dx == enemy_fight_x[t] and dy == enemy_fight_y[t]:
            for i in range(len(characters)):
                while len(characters) > l - 1:
                    player_action = input('Выберете действие: атака, защита, уворот: ')
                    enemy_action = random.choice(['атака', 'защита', 'уворот'])
                    if player_action == 'атака':
                        if enemy_action == 'атака':
                            player_healt -= enemy_attack
                            enemy_healt -= player_attack
                            for lp in range(100):
                                print()
                            print('Вы столкнулись в сокрушительном вихре ударов')
                            print('Вы оба получили урон')
                            print('Здоровье противника:', enemy_healt)
                            print('Ваше здоровье', player_healt)
                        elif enemy_action == 'защита':
                            enemy_healt -= (player_attack - enemy_defance)
                            for lp in range(100):
                                print()
                            print('Противник защитился от вашей атаки и получил лишь часть урона')
                            print('Здоровье противника:', enemy_healt)
                            print('Ваше здоровье', player_healt)
                        elif enemy_action == 'уворот':
                            player_healt -= enemy_attack - player_defance
                            for lp in range(100):
                                print()
                            print('Противник увернулся от вашего удара и пырнул вас')
                            print('Здоровье противника:', enemy_healt)
                            print('Ваше здоровье', player_healt)

                    elif player_action == 'защита':
                        if enemy_action == 'атака':
                            player_healt -= (enemy_attack - player_defance)
                            for lp in range(100):
                                print()
                            print('Вы успешно заблокировали часть урона противника')
                            print('Здоровье противника:', enemy_healt)
                            print('Ваше здоровье', player_healt)
                        elif enemy_action == 'защита':
                            for lp in range(100):
                                print()
                            print('Вы смотрите друг на друга, да, неловко получилось')
                            print('Здоровье противника:', enemy_healt)
                            print('Ваше здоровье', player_healt)
                        elif enemy_action == 'уворот':
                            enemy_healt -= player_attack - enemy_defance
                            for lp in range(100):
                                print()
                            print('Противник попытался увернутся, но вы были готовы')
                            print('Здоровье противника:', enemy_healt)
                            print('Ваше здоровье', player_healt)

                    elif player_action == 'уворот':
                        if enemy_action == 'атака':
                            enemy_healt -= player_attack - enemy_defance
                            for lp in range(100):
                                print()
                            print('Вы ловко ушли из под атаки противника')
                            print('Противник получил урон, в следующий раз он будет умнее.')
                            print('Здоровье противника:', enemy_healt)
                            print('Ваше здоровье', player_healt)
                        elif enemy_action == 'защита':
                            player_healt -= enemy_attack - player_defance
                            for lp in range(100):
                                print()
                            print('Вы увернулись от сокрушительной защиты противника. Так держать.')
                            print('Шутка, противник был готов, и поставил вам подножкуэ')
                            print('Вы получили урон')
                            print('Здоровье противника:', enemy_healt)
                            print('Ваше здоровье', player_healt)
                        elif enemy_action == 'уворот':
                            for lp in range(100):
                                print()
                            print('Вы увернулись от противника, противник увернулся от вас, Искра, буря, безумие.')
                            print('Здоровье противника:', enemy_healt)
                            print('Ваше здоровье', player_healt)


                    if len(characters) > l - 1:
                        if player_healt <= 0:
                            print('Вы проиграли')
                            characters.pop(0)
                            exit(0)
                        if enemy_healt <= 0:
                            characters.pop(t+1)
                            field[enemy_y[t]][enemy_x[t]] = 0
                            enemy_y.pop(t)
                            enemy_x.pop(t)
                            enemy.pop(t)
                            enemy_fight_x[t] = -5
                            enemy_fight_y[t] = -5
                            zas += 1
                            at += 5
                            hp += 20
                            ty = 1

        else:
            print()

print('Вы победили')