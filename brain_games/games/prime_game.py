from random import randint


game_rule = 'prime_game'


# creates one number and checks if it is prime
def get_num_and_result():
    number = randint(2, 100)
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no', number
        divider += 1
    return 'yes', number


# generate lists of mathematical expressions and their answers
def get_prime_lists():
    prime_questions_list, prime_results_list = [], []
    for count in range(1, 4):
        prime_result, number = get_num_and_result()
        prime_questions_list.append(number)
        prime_results_list.append(str(prime_result))
    return prime_questions_list, prime_results_list


# run the create lists function pass its result to the
# variables that the engine imports
prime_questions, prime_results = get_prime_lists()

# pack game variables in one for game engine
prime = game_rule, prime_questions, prime_results
