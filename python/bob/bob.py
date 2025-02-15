def response(hey_bob):
    hey_bob = hey_bob.strip()
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')
    if not hey_bob:
        return 'Fine. Be that way!'
    if is_shout:
        if is_question:
            return "Calm down, I know what I'm doing!"
        return 'Whoa, chill out!'
    if is_question:
        return 'Sure.'
    return 'Whatever.'
