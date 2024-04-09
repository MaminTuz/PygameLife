import random


class Game0flife:
    def __init__(self, width, height):
        self.field = [[0] * width for i in range (height)]


    def intialize(self, life_fraction):
        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                if random.randint(1, 100) <= life_fraction:
                    self.field[y][x] = 1


    def run_transition_rule(self):
        buffer_field = [[0] * len(self.field[0]) for i in range(len(self.field))]
        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                live_neighbors = -1
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if self.field[y + dy][x + dx] == 1:
                            live_neighbors += 1
                if live_neighbors < 2 or live_neighbors > 3:
                    buffer_field[y][x] = 0
                elif live_neighbors == 3:
                    buffer_field[y][x] = 1
                else:
                    buffer_field[y][x] = self.field[y][x]

        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]