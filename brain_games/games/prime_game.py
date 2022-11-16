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
    questions_prime_list = []
    results_prime_list = []
    count = 0
    while count < 3:
        result = get_prime_result()
        questions_prime_list.append(number)
        results_prime_list.append(str(result))
        count += 1
    return questions_prime_list, results_prime_list


def prime_game():
    questions_prime_list, results_prime_list = get_prime_lists()
    body(prime_rule, questions_prime_list, results_prime_list)
