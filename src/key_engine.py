import itertools
import random
import string


def generate_random_key(length):
    """
    It generates a random key of uppercase letters of a given length
    """
    alphabet = string.ascii_uppercase
    return ''.join(random.choice(alphabet) for _ in range(length))


def generate_key_combinations(length):
    """
    It takes a length and returns all possible key combinations of that length
    """
    alphabet = string.ascii_uppercase
    yield from itertools.product(alphabet, repeat=length)


if __name__ == '__main__':
    for _ in range(10):
        print(generate_random_key(5))

    with open('possible_keys.txt', 'w') as f:
        for key in generate_key_combinations(4):
            f.write(f'{key}\n')
