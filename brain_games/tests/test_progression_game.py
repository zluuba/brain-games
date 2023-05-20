from brain_games.games.progression import (
    get_progression, get_question_and_answer
)
from random import seed

seed(1)


def test_get_progression():
    assert get_progression() == (
        [19, 21, 23, 25, 27, 29], 6
    )
    assert get_progression() == (
        [4, 9, 14, 19, 24, 29, 34], 7
    )
    assert get_progression() == (
        [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65], 11
    )


def test_progression_question_generation():
    question, right_answer = get_question_and_answer()
    assert question == '13 .. 19 22 25 28 31 34 37 40'
    assert right_answer == '16'

    question, right_answer = get_question_and_answer()
    assert question == '1 6 11 16 21 26 .. 36'
    assert right_answer == '31'

    question, right_answer = get_question_and_answer()
    assert question == '1 6 11 16 .. 26 31 36 41'
    assert right_answer == '21'
