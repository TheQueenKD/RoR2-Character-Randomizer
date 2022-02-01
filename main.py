import random


CHARACTERS = [
    'captain',
    'engineer',
    'rex',
    'acrid',
    'artificer',
    'bandit',
    'commando',
    'huntress',
    'loader',
    'mercenary',
    'mul-t',
]


def randomizer():
    survivor = random.choice(CHARACTERS)
    print(survivor)


if __name__ == '__main__':
    randomizer()
