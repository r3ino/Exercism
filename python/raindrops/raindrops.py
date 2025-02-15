def convert(number):
    sound = ''
    divider = [3,5,7]
    drop_sound = ['Pling','Plang','Plong']

    for i in range(3):
        if number % divider[i] == 0:
            sound += drop_sound[i]

    if not sound:
        sound = str(number)
    return sound