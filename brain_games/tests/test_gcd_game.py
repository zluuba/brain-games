from brain_games.games.gcd import get_gcd, get_question_and_answer


def test_gcd(set_seed):
    assert get_gcd(1, 4) == 1
    assert get_gcd(3, 9) == 3
    assert get_gcd(4, 22) == 2


def test_gcd_question_generation(set_seed):
    question, right_answer = get_question_and_answer()
    assert question == '5 19'
    assert right_answer == 1

    question, right_answer = get_question_and_answer()
    assert question == '25 3'
    assert right_answer == 1

    question, right_answer = get_question_and_answer()
    assert question == '9 4'
    assert right_answer == 1
