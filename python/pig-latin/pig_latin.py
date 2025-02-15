def translate(text):

    first_letters = ('a','e','i','o','u','xr','yt')
    vowels = 'aeiou'
    consonants = ''

    if text.startswith(first_letters):
        text += 'ay'
        return text

    for letter in text:
        if letter not in vowels:
            consonants += letter
        else:
            break
    remaining_word = text[len(consonants):]
    return remaining_word + consonants + 'ay'

