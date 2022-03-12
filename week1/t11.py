import random


def random_function(y):
    i = 1

    while i <= 5:
        x = int(input('Choose a number between 1 to 20: '))
        i += 1
        if x == y:
            print('You won')
            break
    else:
        print('Game over')


random_function(y=random.randint(1, 20))
