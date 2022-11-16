from random import randint
from brain_games.games_body import body


def progression_rule():
    print('What number is missing in the progression?')


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
    global progression_expression
    progression_expression = " ".join(map(str, final_progression))

    return hide_digit


def get_progression_lists():
    questions_progression_list = []
    results_progression_list = []
    count = 0
    while count < 3:
        result = get_progression_result()
        questions_progression_list.append(progression_expression)
        results_progression_list.append(str(result))
        count += 1
    return questions_progression_list, results_progression_list


def progression():
    questions_list, results_list = get_progression_lists()
    body(progression_rule, questions_list, results_list)
