def translate(text):

    first_letters = ('a','e','i','o','u','xr','yt')
    yowels = ('a','e','i','o','u','y')
    words = text.split()
    translated_text = ''

    for word in words:
        if word.startswith(first_letters):
            word += 'ay'
            translated_text += ' '+ word

        else:
            position_yowels = [word.find(vokal) for vokal in yowels if
                               word.find(vokal) != -1 and (vokal != 'y' or word.find(vokal) > 0)]
            position_yowel = min(position_yowels) if position_yowels else -1

            position_qu = word.find('qu')

            if position_yowel != -1 and (position_qu == -1 or position_yowel < position_qu):
                front_part = word[:position_yowel]
                back_part = word[position_yowel:]

                word = back_part + front_part + 'ay'

            else:
                front_part = text[:position_qu + 2]
                back_part = text[position_qu + 2:]

                word = back_part + front_part + 'ay'

            translated_text += ' ' + word

    return translated_text.strip()