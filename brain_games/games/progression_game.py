from random import randint


game_rule = 'What number is missing in the progression?'


def get_question_and_answer():
    progression, lenght = get_progression()

    hide_char_index = randint(0, lenght - 1)
    right_answer = str(progression[hide_char_index])
    progression[hide_char_index] = '..'

    question = " ".join(map(str, progression))
    return question, right_answer


def get_progression():
    lenght = randint(5, 11)
    start = randint(1, 20)
    step = randint(2, 6)
    stop = start + (lenght * step)
    progression = list(range(start, stop, step))
    return progression, lenght
