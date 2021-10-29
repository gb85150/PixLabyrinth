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
