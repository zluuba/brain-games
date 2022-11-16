import prompt
from random import randint
from brain_games.body import welcome_user, is_correct, lose, win


def progression_rule():
    print('What number is missing in the progression?')


def progression_welcome():
    welcome_user()
    progression_rule()


# showing digit progression with one hide digit
def calculations():
    first_num = randint(1, 20)
    step = randint(2, 6)
    list_volume = randint(5, 11)
    hide_char_index = randint(0, list_volume - 1)
    last_num = first_num + (list_volume * step)

    digit_list = list(range(first_num, last_num, step))
    hide_digit = str(digit_list[hide_char_index])
    digit_list[hide_char_index] = '..'
    global question_list
    question_list = " ".join(map(str, digit_list))
    return hide_digit


def progression():
    i = 0
    while i < 3:
        result = calculations()
        print(f'Question: {question_list}')
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
