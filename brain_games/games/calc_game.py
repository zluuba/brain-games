import random
from random import randint


game_rule = 'calculator_game'


def get_math_expression():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    return num1, num2, operator


def get_math_expression_result():
    num1, num2, operator = get_math_expression()
    expression = f'{num1} {operator} {num2}'
    if operator == "+":
        result_int = num1 + num2
    elif operator == "-":
        result_int = num1 - num2
    else:
        result_int = num1 * num2
    return result_int, expression


def get_calc_lists():
    questions_calc_list = []
    results_calc_list = []
    for count in range(3):
        result, expression = get_math_expression_result()
        questions_calc_list.append(expression)
        results_calc_list.append(str(result))
    return questions_calc_list, results_calc_list


questions, results = get_calc_lists()
