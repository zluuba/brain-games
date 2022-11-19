from random import randint
from brain_games.games_body import body


game_rule = 'prime_game'


def get_prime_result():
    global number
    number = randint(2, 100)
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no'
        divider += 1
    return 'yes'


def get_prime_lists():
    prime_questions_list = []
    prime_results_list = []
    for count in range(3):
        result = get_prime_result()
        prime_questions_list.append(number)
        prime_results_list.append(str(result))
    return prime_questions_list, prime_results_list


def prime_body():
    questions_prime_list, results_prime_list = get_prime_lists()
    body(game_rule, questions_prime_list, results_prime_list)
