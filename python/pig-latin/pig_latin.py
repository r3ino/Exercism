def translate(text):

    first_letters = ('a','e','i','o','u','xr','yt')
    vowels = 'aeiou'
    consonants = ''

    if text.startswith(first_letters):
        text += 'ay'
        return text

    if not text.startswith(first_letters) and not 'qu' in text:
        for letter in text:
            if letter not in vowels:
                consonants += letter
            else:
                break
        remaining_word = text[len(consonants):]
        return remaining_word + consonants + 'ay'

    if 'qu' in text:
        position_qu = text.find('qu')

        if text[position_qu - 1] not in vowels:
            front_part = text[:position_qu + 2]
            back_part = text[position_qu + 2:]

            return back_part + front_part + 'ay'

        for letter in text:
            if letter not in vowels:
                consonants += letter
            else:
                break
        remaining_word = text[len(consonants):]
        return remaining_word + consonants + 'ay'