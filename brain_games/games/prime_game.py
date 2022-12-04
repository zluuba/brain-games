from random import randint


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(2, 100)
    divider = 2
    bool_answer = is_prime(number, divider)
    right_answer = 'yes' if bool_answer else 'no'
    return number, right_answer


def is_prime(number, divider):
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True
