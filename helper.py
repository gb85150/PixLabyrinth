import random
import random as r
from main import game1 as g
from classes import Item


def generate(choice: list, weight: list) -> str:
    """
    :version: 1.0
    Fonction permettant un tirage au sort (random) selon des probabilités fixées sur 100
    :param choice: list of choices
    :param weight: weight of these choices (=probability)
    :return: str (the choice selected)
    """

    coefficient = []
    for i in range(len(choice)):
        coefficient.append([k for k in range(weight[i])])
    result = r.randint(0, 100)
    for i in range(len(choice)):
        if result in coefficient[i]:
            return choice[i]


def generate2(choice: list, weight: list) -> str:
    """
    :param choice: list of choices
    :param weight: weight of these choices
    :return: str
    """
    test = r.choices(choice, weights=tuple(weight))
    return test[0]


def fight():
    hit_list = [
        'fait griffé la jambe',
        'fait attrapé le bras',
        'blessé sur un piège',
        'pris un mur'
    ]
    enemy = g.grid.grid[g.player1.coordinates[1]][g.player1.coordinates[0]].tile.entity

    if input(f"""
=========================================================================================
Mince ! Vous tombez sur un ennemi !
Vous pourriez peut-être courir vers une autre salle...
Pour rappel votre vie est de {g.player1.health} HP.
Voulez-vous combattre ?
""") == 'Y':  # Fight case

        while g.player1.health > 0 or enemy.health > 0:
            # Player1 attack first
            result = g.player1.attacks(enemy)
            print(f"""
⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔
Vous infligez -{result}HP à l'ennemi. Sa vie est d'a présent de {enemy.health}HP.
""")
            result = enemy.attacks(g.player1)
            print(f"""
⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔
L'ennemi vous attaque ! Vous vous faites {random.choices(hit_list)} et vous subissez -{result}HP.
Votre vie s'élève à présent à {g.player1.health}HP.
""")

    else:  # Fleeing case

        if bool(generate2(choice=[True, False], weight=[1, (1 * g.player1.luck)])):
            # Test of the success of the extraction
            result = enemy.attacks(g.player1)
            print(f"""
=========================================================================================
Malheureusement vous vous êtes {random.choices(hit_list)}. Vous subissez {result} dégâts. 
""")

    if Item in g.player1.inv:  # Verification de l'inventaire
        for i in range(len(g.player1.inv)):
            if g.player1.inv[i].category == 'potion':
                if g.player1.health < 25:
                    if input("""
=========================================================================================
Vous êtes à l'abri, voulez-vous vous soigner (Y/N)?                   
""") == 'Y':
                        g.player1.heal()
            if g.player1.inv[i].category == 'weapon':
                if input("""
                =========================================================================================
                Vous êtes à l'abri, vous avez trouvé un arme. Voulez-vous l'équiper (Y/N)?                   
                """) == 'Y':
                    g.player1.attack += g.player1.inv[i].attack


# wondering about moving this to Grid class ?
def print_grid(grid) -> None:
    for i in range(len(grid)):
        print(("┌───┐\n│   │\n└───┘\n" * len(grid[i])), sep=' ')
        return None
