def square(number):
    if not (1 <= number <= 64):
        raise ValueError('square must be between 1 and 64')

    return 2 ** (number - 1)


def total():
    toto: int = 0

    for i in range(64):
        toto = toto + 2 ** i

    return toto