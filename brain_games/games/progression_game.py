from random import randint


game_rule = 'progression_game'


# creates an arithmetic sequence with one hide number.
# Example: '12, 15, 18, .., 21, 24'
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

    # create progression what user see (with hide char)
    progression_expression = " ".join(map(str, final_progression))

    return hide_digit, progression_expression


# generate lists of mathematical expressions and their answers
def get_progression_lists():
    progression_questions_list = []
    progression_results_list = []
    for count in range(1, 4):
        result, progression_expression = get_progression_result()
        progression_questions_list.append(progression_expression)
        progression_results_list.append(str(result))
    return progression_questions_list, progression_results_list


# run the create lists function pass its result to the
# variables that the engine imports
questions, results = get_progression_lists()

# pack game variables in one for game engine
progression = game_rule, questions, results
