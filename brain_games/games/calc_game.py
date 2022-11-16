import random
from random import randint
from brain_games.body import welcome_user, question, is_correct, lose, win


def calc_rule():
    print('What is the result of the expression?')


def calc_welcome():
    welcome_user()
    calc_rule()


def get_expression():
    global num1, num2, operator, expression
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    expression = f'{num1} {operator} {num2}'


def get_result():
    get_expression()
    if operator == "+":
        result_int = num1 + num2
    elif operator == "-":
        result_int = num1 - num2
    else:
        result_int = num1 * num2
    return result_int


def calculator():
    count = 0
    while count < 3:
        result = str(get_result())
        answer = question(expression)
        correct = is_correct(answer, result)
        if correct:
            count += 1
            continue
        else:
            lose()
            break
    else:
        win()
