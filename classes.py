from helper import generate


class Grid:
    def __init__(self, x, y):
        self.grid = []
        tmp = []
        for i in range(y):
            for k in range(x):
                tmp.append(Tile())
            self.grid.append(tmp)

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
    def __init__(self, attack: int, type: str, benefit: int, disposable: bool):
        if type == 'weapon':
            self.attack = attack
        if type == 'potion':
            self.benefit = benefit
        self.type = type
        self.disposable = disposable


class Character:
    """
    Can be a player, an enemy or an NPC
    :param health: number of health points
    :param attack: number of damage given per hit
    :param luck: critical damage probability
    :param inv: inventory of the character, looted on death
    """
    def __init__(self, health: int, attack: int, luck: int, inv: list) -> None:
        self.health = health
        self.attack = attack
        self.luck = luck
        self.inv = inv
