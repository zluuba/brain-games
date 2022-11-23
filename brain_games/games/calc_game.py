import random
from operator import add, sub, mul
from random import randint


game_rule = 'What is the result of the expression?'


# create random numbers and get random operator from dictionary
# count the result and pass all of this to get_expression
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


# create one simple math expression, calculate the result
def get_expression():
    num1, num2, operator_, result = get_expression_parts_and_result()
    expression = f'{num1} {operator_} {num2}'
    return result, expression


# generate lists of mathematical expressions and their answers
def get_calc_lists():
    questions_calc_list = []
    results_calc_list = []
    for _ in range(3):
        result, expression = get_expression()
        questions_calc_list.append(expression)
        results_calc_list.append(str(result))
    return questions_calc_list, results_calc_list


# run the create lists function pass its result to the
# variables that the engine imports
calc_questions, calc_results = get_calc_lists()

# pack game variables in one for game engine
calculator = game_rule, calc_questions, calc_results
