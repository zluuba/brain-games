from brain_games.games.gcd import get_gcd, get_question_and_answer
from random import seed

seed(2)


def test_gcd():
    assert get_gcd(1, 4) == 1
    assert get_gcd(3, 9) == 3
    assert get_gcd(4, 22) == 2


def test_gcd_question_generation():
    question, right_answer = get_question_and_answer()
    assert question == '2 3'
    assert right_answer == 1

    question, right_answer = get_question_and_answer()
    assert question == '3 12'
    assert right_answer == 3

    question, right_answer = get_question_and_answer()
    assert question == '6 24'
    assert right_answer == 6
