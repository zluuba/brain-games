from random import randint
from brain_games.games.body import *
import prompt


def gcd_game_rule():
    print('Find the greatest common divisor of given numbers.')


def calculations():
    calculation = ''
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    global nums
    nums = f'{num1} {num2}'

    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
        calculation = num1 + num2
    return calculation


def greatest_cd():
    global result, answer, correct
    i = 0
    while i < 3:
        result = str(calculations())
        print(f'Question: {nums}')
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
