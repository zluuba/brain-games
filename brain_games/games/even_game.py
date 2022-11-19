from random import randint


game_rule = 'even_game'


def get_num_and_result():
    num = randint(0, 25)
    result = num % 2 == 0 and "yes" or "no"
    return num, result


def get_even_lists():
    questions_even_list = []
    results_even_list = []
    for count in range(3):
        num, result = get_num_and_result()
        questions_even_list.append(num)
        results_even_list.append(str(result))
    return questions_even_list, results_even_list


questions, results = get_even_lists()
