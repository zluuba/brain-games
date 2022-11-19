from random import randint


game_rule = 'progression_game'


def get_progression_result():
    # create simple variables for future calculation
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

    # create progression what user see
    progression_expression = " ".join(map(str, final_progression))

    return hide_digit, progression_expression


def get_progression_lists():
    questions_progression_list = []
    results_progression_list = []
    for count in range(3):
        result, progression_expression = get_progression_result()
        questions_progression_list.append(progression_expression)
        results_progression_list.append(str(result))
    return questions_progression_list, results_progression_list


questions, results = get_progression_lists()
