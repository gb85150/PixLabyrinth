import random as r


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
    # TODO: Make fight function
    pass


def move(direction: str, coord: list) -> list:
    """
    Move the player in the specified direction
    :param direction: str, can be either : south, north, east or west
    :param coord: the current coordinates of the player
    :return: the new coordinates
    """
    # TODO: Update coordinates directly to the instance
    # TODO: Check for 'out of map' issues
    if direction == 'south':
        coord[0] += 0
        coord[1] += -1
        return coord
    elif direction == 'north':
        coord[0] += 0
        coord[1] += 1
        return coord
    elif direction == 'east':
        coord[0] += 1
        coord[1] += 0
        return coord
    else:
        coord[0] += -1
        coord[1] += 0
        return coord


def print_grid(grid) -> None:
    for i in range(len(grid)):
        print(("┌───┐\n│   │\n└───┘\n" * len(grid[i])), sep=' ')
        return None
