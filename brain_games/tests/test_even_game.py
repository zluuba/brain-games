from brain_games.games.even import get_question_and_answer


def test_even_question_generation(set_seed):
    question, right_answer = get_question_and_answer()
    assert question == 4
    assert right_answer == 'yes'

    question, right_answer = get_question_and_answer()
    assert question == 18
    assert right_answer == 'yes'

    question, right_answer = get_question_and_answer()
    assert question == 25
    assert right_answer == 'no'
