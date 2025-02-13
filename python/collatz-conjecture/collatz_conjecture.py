def steps(number):
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    counter = 0

    while number != 1:
        if number % 2 == 0:
            number = number / 2
            counter = counter + 1
        else:
            number = number * 3 + 1
            counter = counter +1

    return counter