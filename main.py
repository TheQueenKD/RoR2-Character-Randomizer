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
    players = int(input('How many players? (Default: 2) ') or 2)
    print()
    for player in range(1, 1 + players):
        print(f'Player {player} you should play: {get_survivor()}')
