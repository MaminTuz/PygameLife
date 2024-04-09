from Laba8 import *
import pygame

def render_pygame(field, scr, scale):
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                pygame.draw.rect(scr, (255, 255, 255), (x * scale, y * scale, scale, scale))
            elif field[y][x] == 1:
                pygame.draw.rect(scr, (0, 0, 255), (x * scale, y * scale, scale, scale))
            pygame.draw.rect(scr, (0, 0, 0), (x * scale, y * scale, scale, scale), 2)

def main():
    a = int(input('Введите длину поля: '))
    b = int(input('Введите ширину поля: '))
    c = int(input('Введите количество живых клеток: '))
    scale = int(input('Введите размер клеток при отрисовке'))
    gof = Game0flife(a, b)
    gof.intialize(c)


    pygame.init()
    screen = pygame.display.set_mode((a * scale, b * scale))
    pygame.display.set_caption("Game of life")
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        gof.run_transition_rule()
        screen.fill((0, 0, 0))
        render_pygame(gof.field, screen, scale)
        pygame.display.flip()
        clock.tick(60)



if __name__ == '__main__':
    main()
