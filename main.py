from Laba_8_ly import *


def render_field(field):
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                print(' ', end='')
            elif field[y][x] == 1:
                print('X', end='')
        print()
    print('---------------------------------')

def main():
    gof = Game0flife(30, 30)
    gof.intialize(30)
    for i in range(30):
        gof.run_transition_rule()
        render_field(gof.field)

if __name__ == '__main__':
    main()

