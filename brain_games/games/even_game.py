from random import randint


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_answer_and_question():
    number = randint(0, 25)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return right_answer, number
