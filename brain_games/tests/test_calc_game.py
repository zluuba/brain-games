from brain_games.games.calc import get_question_and_answer
from random import seed

seed(1)


def test_calc_question_generation():
    question, right_answer = get_question_and_answer()
    assert question == '5 + 19'
    assert right_answer == 24

    question, right_answer = get_question_and_answer()
    assert question == '9 - 4'
    assert right_answer == 5

    question, right_answer = get_question_and_answer()
    assert question == '25 - 15'
    assert right_answer == 10
