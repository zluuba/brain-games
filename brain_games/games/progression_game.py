from random import randint


game_rule = 'What number is missing in the progression?'


def get_result_and_question():
    lenght = randint(5, 11)
    start = randint(1, 20)
    step = randint(2, 6)
    progression = list(range(start, start + (lenght * step), step))

    hide_char_index = randint(0, lenght - 1)
    hidden_digit = str(progression[hide_char_index])
    progression[hide_char_index] = '..'

    question = " ".join(map(str, progression))
    return hidden_digit, question
