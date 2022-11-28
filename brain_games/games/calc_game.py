import random
from operator import add, sub, mul
from random import randint
from brain_games.games_body import num_of_rounds


game_rule = 'What is the result of the expression?'


def get_expression_parts_and_result():
    num1, num2 = randint(1, 25), randint(1, 25)
    operators_dictionary = {
        "+": add(num1, num2),
        "-": sub(num1, num2),
        "*": mul(num1, num2)
    }
    operator_ = random.choice(list(operators_dictionary.keys()))
    result = operators_dictionary[operator_]
    return num1, num2, operator_, result


def get_expression():
    num1, num2, operator_, result = get_expression_parts_and_result()
    expression = f'{num1} {operator_} {num2}'
    return result, expression


# generate lists of expressions and their answers
def get_calc_lists():
    questions_calc_list = []
    results_calc_list = []
    for _ in range(num_of_rounds):
        result, expression = get_expression()
        questions_calc_list.append(expression)
        results_calc_list.append(str(result))
    return questions_calc_list, results_calc_list


calc_questions, calc_results = get_calc_lists()

# pack game variables in one for game engine
calculator = game_rule, calc_questions, calc_results
