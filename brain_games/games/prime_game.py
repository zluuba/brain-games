from random import randint


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_answer_and_question():
    number = randint(2, 100)
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no', number
        divider += 1
    return 'yes', number
