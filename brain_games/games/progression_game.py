from random import randint


game_rule = 'What number is missing in the progression?'


def get_result_and_expression():
    step = randint(2, 6)
    progression_lenght = randint(5, 11)
    hide_char_index = randint(0, progression_lenght - 1)
    first_num = randint(1, 20)
    last_num = first_num + (progression_lenght * step)

    # create final progression and hide char
    progression = list(range(first_num, last_num, step))
    hide_digit = str(progression[hide_char_index])
    progression[hide_char_index] = '..'
    expression = " ".join(map(str, progression))
    return hide_digit, expression
