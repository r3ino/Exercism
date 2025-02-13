def is_armstrong_number(number):
    if number < 0:
        raise ValueError('Only positive Integers are allowed!')

    ziffern = [int(digit) for digit in str(number)]

    anzahl_ziffern = len(ziffern)

    summe = sum(digit ** anzahl_ziffern for digit in ziffern)

    return summe == number