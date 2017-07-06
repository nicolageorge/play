import random

def one_two():
    return random.randint(1, 2)

def one_two_three():
    while one_two() == 1:
        while one_two() == 2:
            return 3
    return one_two()
