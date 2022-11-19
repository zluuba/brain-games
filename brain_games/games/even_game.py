from random import randint


game_rule = 'even_game'


def get_result():
    global number
    number = randint(1, 25)
    return number % 2 == 0 and "yes" or "no"


def get_even_lists():
    questions_even_list = []
    results_even_list = []
    for count in range(3):
        result = get_result()
        questions_even_list.append(number)
        results_even_list.append(str(result))
    return questions_even_list, results_even_list


questions, results = get_even_lists()
