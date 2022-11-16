import prompt
from random import randint
from brain_games.body import welcome_user, is_correct, lose, win


def even_rule():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def even_welcome():
    welcome_user()
    even_rule()


def calculations():
    calculation = ''
    global number
    number = randint(1, 20)
    if number % 2 == 0:
        calculation += 'yes'
    else:
        calculation += 'no'
    return calculation


def is_even_game():
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
