from random import randint
from brain_games.games.body import *
import prompt


def game_rule():
    print('What number is missing in the progression?')


# showing digit progression with one hide digit
def calculations():
    first_digit = randint(1, 20)
    step = randint(2, 6)
    list_volume = randint(5, 11)
    hide_digit = randint(0, list_volume - 1)
    digit_list = list(range(first_digit, first_digit + (list_volume * step), step))
    calculations = str(digit_list[hide_digit])
    digit_list[hide_digit] = '..'
    global l
    l = " ".join(map(str, digit_list))
    return calculations


def progression():
    global result, answer, correct
    i = 0
    while i < 3:
        result = calculations()
        print(f'Question: {l}')
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
