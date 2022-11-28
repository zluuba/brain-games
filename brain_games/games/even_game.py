from random import randint
from brain_games.games_body import num_of_rounds


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_num_and_result():
    num = randint(0, 25)
    result = 'yes' if num % 2 == 0 else 'no'
    return num, result


# generate lists of expressions and their answers
def get_even_lists():
    list_with_questions = []
    list_with_results = []
    for _ in range(num_of_rounds):
        num, result = get_num_and_result()
        list_with_questions.append(num)
        list_with_results.append(str(result))
    return list_with_questions, list_with_results


even_questions, even_results = get_even_lists()

# pack game variables in one for game engine
even = game_rule, even_questions, even_results
