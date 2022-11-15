from random import randint
from brain_games.body import is_correct, lose, win
import prompt


def prime_rule():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def calculations():
    global number
    number = randint(2, 100)
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no'
        divider += 1
    return 'yes'


def prime_game():
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
