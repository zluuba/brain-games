from random import randint
from brain_games.games.body import *
import prompt


def game_rule():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def calculations():
    calculations = ''
    global number
    number = randint(1, 20)
    if number % 2 == 0:
        calculations += 'yes'
    else:
        calculations += 'no'
    return calculations


def is_even_game():
    global result, answer, correct
    i = 0
    while i < 3:
        result = calculations()
        print(f'Question: {number}')
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
