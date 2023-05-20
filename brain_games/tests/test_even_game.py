from brain_games.games.even import get_question_and_answer
from random import seed

seed(1)


def test_even_question_generation():
    question, right_answer = get_question_and_answer()
    assert question == 4
    assert right_answer == 'yes'

    question, right_answer = get_question_and_answer()
    assert question == 18
    assert right_answer == 'yes'

    question, right_answer = get_question_and_answer()
    assert question == 25
    assert right_answer == 'no'
