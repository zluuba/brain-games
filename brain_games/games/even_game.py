from random import randint


game_rule = 'even_game'


def get_result():
    number = randint(0, 25)
    result = number % 2 == 0 and "yes" or "no"
    return number, result


def get_even_lists():
    questions_even_list = []
    results_even_list = []
    for count in range(3):
        number, result = get_result()
        questions_even_list.append(number)
        results_even_list.append(str(result))
    return questions_even_list, results_even_list


questions, results = get_even_lists()
