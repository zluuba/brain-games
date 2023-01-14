from random import randint


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(2, 100)
    number_is_prime = is_prime(number)
    right_answer = 'yes' if number_is_prime else 'no'
    return number, right_answer


def is_prime(number):
    for divider in range(2, (number // 2) + 1):
        if number % divider == 0:
            return False
    return True
