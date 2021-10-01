import random as r


def generate(choice: list, weight: list):
    for i in range(len(choice)):
        coefficient = [k for k in range(weight[i])]
    result = r.randint(0, 100)
    for i in range(len(choice)):
        if result in coefficient[i]:
            return choice[i]
    pass
