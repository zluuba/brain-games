from brain_games.games.calc import get_question_and_answer


def test_calc_question_generation(set_seed):
    question, right_answer = get_question_and_answer()
    assert question == '5 + 19'
    assert right_answer == 24

    question, right_answer = get_question_and_answer()
    assert question == '9 - 4'
    assert right_answer == 5

    question, right_answer = get_question_and_answer()
    assert question == '25 - 15'
    assert right_answer == 10
