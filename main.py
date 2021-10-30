import random

from classes import *

# from helper import print_grid

"⚔💰🌀👑"
"""
┌───┐
│   │
│ x │
│   │
└───┘
"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO: Reorder code and write main code (Warning : don't include functions here)
    game1 = Game()
    while game1.player1.health > 0 or game1.player1.coordinates != game1.grid.issue_pos:
        game1.ask_next_move()
        game1.new_tile_event()


def fight():
    hit_list = [
        'fait griffé la jambe',
        'fait attrapé le bras',
        'blessé sur un piège',
        'pris un mur'
    ]
    enemy = game1.grid.grid[game1.player1.coordinates[1]][game1.player1.coordinates[0]].tile.entity

    if input(f"""
=========================================================================================
Mince ! Vous tombez sur un ennemi !
Vous pourriez peut-être courir vers une autre salle...
Pour rappel votre vie est de {game1.player1.health} HP.
Voulez-vous combattre ?
""") == 'Y':  # Fight case

        while game1.player1.health > 0 or enemy.health > 0:
            # Player1 attack first
            result = game1.player1.attacks(enemy)
            print(f"""
⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔
Vous infligez -{result}HP à l'ennemi. Sa vie est d'a présent de {enemy.health}HP.
""")
            result = enemy.attacks(game1.player1)
            print(f"""
⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔
L'ennemi vous attaque ! Vous vous faites {random.choices(hit_list)} et vous subissez -{result}HP.
Votre vie s'élève à présent à {game1.player1.health}HP.
""")

    else:  # Fleeing case

        if bool(generate2(choice=[True, False], weight=[1, (1 * game1.player1.luck)])):
            # Test of the success of the extraction
            result = enemy.attacks(game1.player1)
            print(f"""
=========================================================================================
Malheureusement vous vous êtes {random.choices(hit_list)}. Vous subissez {result} dégâts. 
""")

    if Item in game1.player1.inv:  # Verification de l'inventaire
        for i in range(len(game1.player1.inv)):
            if game1.player1.inv[i].category == 'potion':
                if game1.player1.health < 25:
                    if input("""
=========================================================================================
Vous êtes à l'abri, voulez-vous vous soigner (Y/N)?                   
""") == 'Y':
                        game1.player1.heal()
            if game1.player1.inv[i].category == 'weapon':
                if input("""
                =========================================================================================
                Vous êtes à l'abri, vous avez trouvé un arme. Voulez-vous l'équiper (Y/N)?                   
                """) == 'Y':
                    game1.player1.attack += game1.player1.inv[i].attack
