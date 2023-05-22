from brain_games.games.prime import is_prime, get_question_and_answer


def test_is_prime(set_seed):
    assert is_prime(5)
    assert is_prime(7)
    assert not is_prime(20)


def test_prime_question_generation(set_seed):
    question, right_answer = get_question_and_answer()
    assert question == 19
    assert right_answer == 'yes'

    question, right_answer = get_question_and_answer()
    assert question == 74
    assert right_answer == 'no'

    question, right_answer = get_question_and_answer()
    assert question == 99
    assert right_answer == 'no'
