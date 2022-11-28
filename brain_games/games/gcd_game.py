from random import randint
from brain_games.games_body import num_of_rounds


game_rule = 'Find the greatest common divisor of given numbers.'


def get_numbers():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    return num1, num2


def get_expression():
    num1, num2 = get_numbers()
    expression = f'{num1} {num2}'
    return num1, num2, expression


# find the greatest common divisor(gcd)
def get_gcd_result():
    num1, num2, expression = get_expression()
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    result = num2
    return result, expression


# generate lists of expressions and their answers
def get_gcd_lists():
    questions_gcd_list = []
    results_gcd_list = []
    for _ in range(num_of_rounds):
        result, expression = get_gcd_result()
        questions_gcd_list.append(expression)
        results_gcd_list.append(str(result))
    return questions_gcd_list, results_gcd_list


gcd_questions, gcd_results = get_gcd_lists()

# pack game variables in one for game engine
gcd = game_rule, gcd_questions, gcd_results
