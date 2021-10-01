from random import randrange


class Grid:
    def __init__(self, x, y):
        grid = []
        for i in range(x):
            for k in range(y):
                grid.append(Tile())


class Tile:
    def __init__(self):
        generate()
        pass
