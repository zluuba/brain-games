import random
from random import randint
from brain_games.games.body import *
import prompt


def calc_game_rule():
    print('What is the result of the expression?')


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
    global result, answer, correct
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
