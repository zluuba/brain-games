from random import randint
from brain_games.games_body import body


def even_rule():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_number():
    global number
    number = randint(1, 25)


def get_result():
    get_number()
    if number % 2 == 0:
        result = "yes"
    else:
        result = "no"
    return result


def get_even_lists():
    counter = 1
    questions_even_list = []
    results_even_list = []
    while counter <= 3:
        result = get_result()
        questions_even_list.append(number)
        results_even_list.append(str(result))
        counter += 1
    return questions_even_list, results_even_list


def is_even_game():
    questions_even_list, results_even_list = get_even_lists()
    body(even_rule, questions_even_list, results_even_list)
