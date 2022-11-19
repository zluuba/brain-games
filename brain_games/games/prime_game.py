from random import randint


game_rule = 'prime_game'


def get_prime_result():
    number = randint(2, 100)
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no', number
        divider += 1
    return 'yes', number


def get_prime_lists():
    prime_questions_list = []
    prime_results_list = []
    for count in range(3):
        result, number = get_prime_result()
        prime_questions_list.append(number)
        prime_results_list.append(str(result))
    return prime_questions_list, prime_results_list


questions, results = get_prime_lists()
