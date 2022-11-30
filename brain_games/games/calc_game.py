import random
from operator import add, sub, mul
from random import randint


game_rule = 'What is the result of the expression?'


def get_answer_and_question():
    num1, num2 = randint(1, 25), randint(1, 25)
    operators_dictionary = {
        "+": add(num1, num2),
        "-": sub(num1, num2),
        "*": mul(num1, num2)
    }
    operator_ = random.choice(list(operators_dictionary.keys()))
    right_answer = operators_dictionary[operator_]
    question = f'{num1} {operator_} {num2}'
    return right_answer, question
