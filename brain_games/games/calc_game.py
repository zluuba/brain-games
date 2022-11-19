import random
from random import randint
from brain_games.games_body import body


game_rule = 'calculator_game'


def get_math_expression():
    global num1, num2, operator, expression
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    expression = f'{num1} {operator} {num2}'


def get_math_expression_result():
    get_math_expression()
    if operator == "+":
        result_int = num1 + num2
    elif operator == "-":
        result_int = num1 - num2
    else:
        result_int = num1 * num2
    return result_int


def get_calc_lists():
    questions_calc_list = []
    results_calc_list = []
    count = 0
    while count < 3:
        result = get_math_expression_result()
        questions_calc_list.append(expression)
        results_calc_list.append(str(result))
        count += 1
    return questions_calc_list, results_calc_list


def calculator_body():
    questions_list, results_list = get_calc_lists()
    body(game_rule, questions_list, results_list)
