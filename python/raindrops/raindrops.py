def convert(number):
    pass

    for i in range(3):
        if number % divider[i] == 0:
            sound += drop_sound[i]

    if not sound:
        sound = str(number)
    return sound