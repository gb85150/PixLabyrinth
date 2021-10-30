import main
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
""")).lower()
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

        print('Generating... Please wait')
        self.grid.print_dev_grid()

    def ask_next_move(self) -> None:
        print(f"""
=========================================================================================
Vous vous situez en {self.player1.coordinates}.
La sortie se situe dans le coin inférieur droit en {self.grid.issue_pos}.
Où désirez-vous vous rendre ?
""")
        direction = input('Direction ? (south/north/east/west) : ').lower()
        self.player1.move(direction)

    def new_tile_event(self):
        tile_type = self.grid.grid[self.player1.coordinates[1] - 1][self.player1.coordinates[0] - 1].tile_type

        if tile_type == 'fight':
            main.fight()

        elif tile_type == 'loot':
            raise NotImplementedError('Not implemented yet, sorry for the inconvenience')

        elif tile_type == 'money':
            revenue = self.player1.earn_money()
            print(f"""
=========================================================================================
Félicitations, vous avez trouvé de l'argent ({revenue}, votre argent s'élève à présent à {self.player1.balance}.
""")

        else:
            print("""
=========================================================================================
La salle est vide ! Vous pouvez vous re-déplacer.
""")


class Grid:
    def __init__(self, x, y):
        self.grid = []
        for i in range(y):
            line = []
            for k in range(x):
                line.append(Tile())
            self.grid.append(line)
        self.issue_pos = (len(self.grid[0]), len(self.grid[len(self.grid) - 1]))

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
                health=10,
                attack=1,
                luck=int(generate2([1, 2, 3], [60, 40, 20])),
                inv=[],
                xy=[]
            )
            # TODO: Add loot generation

        elif self.tile_type == 'money':
            # The money is now managed in Character class
            pass

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
        self.balance = 0
        self.health = health
        self.attack = attack
        self.luck = luck
        self.inv = inv
        self.coordinates = xy

    def heal(self):
        # TODO: Healing
        pass

    def move(self, direction: str):
        """
        Move the player in the specified direction
        :param direction: str, can be either : south, north, east or west
        :param self: self, used for updating the position
        """
        # TODO: Check for 'out of map' issues

        if direction == 'south':
            self.coordinates[0] += 0
            self.coordinates[1] += -1

        elif direction == 'north':
            self.coordinates[0] += 0
            self.coordinates[1] += 1

        elif direction == 'east':
            self.coordinates[0] += 1
            self.coordinates[1] += 0

        else:
            self.coordinates[0] += -1
            self.coordinates[1] += 0

    def earn_money(self) -> float:
        loot_table = [2, 5, 10, 25]
        probability_table = [10, 20, 15, 5]
        base_earnings = int(generate2(choice=loot_table, weight=probability_table))
        total_earnings = base_earnings + base_earnings * (self.luck / 10)
        self.balance += total_earnings
        return total_earnings

    def attacks(self, target) -> int:

        if bool(generate2(choice=[True, False], weight=[(1*target.luck), 1])):  # True if the enemy avoid the attack
            return 0

        else:

            if generate2(choice=[True, False], weight=[(1*self.luck), 4]):  # Critical Hit

                target.health -= self.attack * 2
                return self.attack * 2

            else:  # Regular hit

                target.health -= self.attack
                return self.attack
