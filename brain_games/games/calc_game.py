import prompt
import random
from random import randint
from brain_games.body import welcome_user, is_correct, lose, win


def calc_rule():
    print('What is the result of the expression?')


def calc_welcome_game():
    welcome_user()
    calc_rule()


def calculations():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    global question
    question = f'{num1} {operator} {num2}'

    if operator == "+":
        calculation = num1 + num2
    elif operator == "-":
        calculation = num1 - num2
    else:
        calculation = num1 * num2
    return calculation


def calculator():
    i = 0
    while i < 3:
        result = str(calculations())
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correct = is_correct(answer, result)
        if correct:
            i += 1
            continue
        else:
            lose()
            break
    else:
        win()
