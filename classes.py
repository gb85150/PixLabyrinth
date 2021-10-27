from random import randint
from helper import generate2


class Game:
    """Main Class, can be used for saving game slots"""

    def __init__(self) -> None:
        """
        The first module.
        It ask the player for the future settings and prepare the game.
        :return None:
        """
        # Asking the player for parameters
        x = int(input("""Quelle est la largeur de la grille de jeu ?
Largeur :
"""))
        y = int(input(f"""
Quelle est la hauteur de la grille de jeu ? Pour Rappel, sa largeur est de {x} case de largeur.
Hauteur :
"""))
        grid_size = (x, y)
        difficulty = str(input("""
Difficulté (easy, medium, hard) :
"""))
        # Setting up the game (NB: this part can be moved to another function if we make globals
        self.grid = Grid(grid_size[0], grid_size[1])

        if difficulty == 'easy':
            self.player1 = Character(health=25, attack=5, luck=2, inv=[], xy=[0, 0])
        elif difficulty == 'medium':
            self.player1 = Character(health=20, attack=3, luck=1, inv=[], xy=[0, 0])
        elif difficulty == 'hard':
            self.player1 = Character(health=15, attack=2, luck=0, inv=[], xy=[0, 0])
        else:
            raise TypeError("Une difficulté inconnue à été spécifiée")

        self.grid.print_dev_grid()


class Grid:
    def __init__(self, x, y):
        self.grid = []
        # TODO: Fix generation (Loop executed 2 times)
        for i in range(y):
            line = []
            for k in range(x):
                line.append(Tile())
            self.grid.append(line)

    def print_dev_grid(self) -> None:
        view = []
        for i in range(len(self.grid)):
            line = []
            for k in range(len(self.grid[0])):
                line.append(self.grid[i][k].get())
            view.append(line)
        print(len(view))
        for i in range(len(view)):
            print(f"{view[i]}\r")
        return None


class Tile:
    def __init__(self):
        self.tile_type = generate2(['void', 'money', 'loot', 'fight'], [10, 10, 30, 50])
        # On génère la map théorique...
        # Génération des instances des ennemis
        if self.tile_type == 'void':
            # Do nothing
            pass
        elif self.tile_type == 'fight':
            self.entity = Character(
                health=10, attack=1, luck=int(generate2([1, 2, 3], [60, 40, 20])), inv=[], xy=[])
            # TODO: Add loot generation
        elif self.tile_type == 'money':
            self.value = randint(2, 20)
            # TODO: Set Money Management
        elif self.tile_type == 'loot':
            # TODO: Generate loot (See line 34)
            pass

    def get(self):
        print(self.tile_type)
        return self.tile_type


class Item:
    def __init__(self, attack: int, category: str, benefit: int, disposable: bool):
        if category == 'weapon':
            self.attack = attack
        if category == 'potion':
            self.benefit = benefit
        self.category = category
        self.disposable = disposable


class Character:
    """
    Can be a player, an enemy or an NPC
    :param health: number of health points
    :param attack: number of damage given per hit
    :param luck: critical damage probability
    :param inv: inventory of the character, looted on death
    :param xy: position of the character
    """
    def __init__(self, health: int, attack: int, luck: int, inv: list, xy: list) -> None:
        self.health = health
        self.attack = attack
        self.luck = luck
        self.inv = inv
        self.coordinates = xy

    def heal(self):
        # TODO: Healing
        pass
