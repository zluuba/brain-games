from random import randint


game_rule = 'What number is missing in the progression?'


def get_result_and_expression():
    first_num = randint(1, 20)
    step = randint(2, 6)
    list_volume = randint(5, 11)

    # create hide char index and last number of progression for range function
    hide_char_index = randint(0, list_volume - 1)
    last_num = first_num + (list_volume * step)

    # create final progression and hide char
    final_progression = list(range(first_num, last_num, step))
    hide_digit = str(final_progression[hide_char_index])
    final_progression[hide_char_index] = '..'

    # create progression what user see (with hide char)
    progression_expression = " ".join(map(str, final_progression))

    return hide_digit, progression_expression
