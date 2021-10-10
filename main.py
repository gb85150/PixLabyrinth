from classes import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO: Reorder code and write main code (Warning : don't include functions here)
    grid1 = Grid(7, 7)
    player1 = Character(health=20, attack=3, luck=0, inv=[], xy=[0, 0])
    grid1.print_grid()
