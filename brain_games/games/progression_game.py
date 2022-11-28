from random import randint
from brain_games.games_body import num_of_rounds


game_rule = 'What number is missing in the progression?'


# creates sequence with one hide number
def get_progression_result():
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


# generate lists of expressions and their answers
def get_progression_lists():
    questions_list = []
    results_list = []
    for _ in range(num_of_rounds):
        result, progression_expression = get_progression_result()
        questions_list.append(progression_expression)
        results_list.append(str(result))
    return questions_list, results_list


questions, results = get_progression_lists()

# pack game variables in one for game engine
progression = game_rule, questions, results
