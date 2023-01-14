from random import randint


game_rule = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    right_answer = get_gcd(num1, num2)
    question = f'{num1} {num2}'
    return question, right_answer


def get_gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
