from random import randint
from brain_games.body import welcome_user, question, is_correct, lose, win


def even_rule():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def even_welcome():
    welcome_user()
    even_rule()


def get_even_result():
    global number
    number = randint(1, 25)
    return number % 2 == 0 and 'yes' or 'no'


def is_even_game():
    count = 0
    while count < 3:
        result = get_even_result()
        answer = question(number)
        correct = is_correct(answer, result)
        if correct:
            count += 1
            continue
        else:
            lose()
            break
    else:
        win()
