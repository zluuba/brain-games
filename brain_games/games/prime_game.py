from random import randint
from brain_games.games_body import body


def prime_rule():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


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
    count = 0
    prime_questions_list = []
    prime_results_list = []
    while count < 3:
        result = get_prime_result()
        prime_questions_list.append(number)
        prime_results_list.append(str(result))
        count += 1
    return prime_questions_list, prime_results_list


def prime_game():
    questions_prime_list, results_prime_list = get_prime_lists()
    body(prime_rule, questions_prime_list, results_prime_list)
