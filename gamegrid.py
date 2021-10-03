from helper import generate


class Grid:
    def __init__(self, x, y):
        self.grid = []
        for i in range(y):
            for k in range(x):
                self.grid[i].append(Tile())

    def print_grid(self) -> None:
        view = []
        for i in range(len(self.grid[0])):
            for k in range(len(self.grid)):
                view.append(self.grid[i][k].get())
        return print(view)


class Tile:
    def __init__(self):
        self.tile_type = generate(['void', 'money', 'loot', 'fight'], [10, 10, 30, 50])

    def get(self):
        print(self.tile_type)
        return self.tile_type


class Item:
    def __init__(self):
        pass


class Character:
    def __init__(self):
        pass
