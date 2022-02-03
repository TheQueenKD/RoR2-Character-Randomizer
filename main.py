import random


CHARACTERS = [
    'Captain',
    'Engineer',
    'Rex',
    'Acrid',
    'Artificer',
    'Bandit',
    'Commando',
    'Huntress',
    'Loader',
    'Mercenary',
    'MUL-T',
]


def get_survivor():
    return random.choice(CHARACTERS)


if __name__ == '__main__':
    print(f'You should play: {get_survivor()}')
