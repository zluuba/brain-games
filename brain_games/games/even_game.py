from random import randint


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_result_and_expression():
    num = randint(0, 25)
    result = 'yes' if num % 2 == 0 else 'no'
    return result, num
