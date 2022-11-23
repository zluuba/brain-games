from random import randint


game_rule = 'Find the greatest common divisor of given numbers.'


# creates two numbers and finds the Greatest Common Divisor (gcd)
def get_gcd_result():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    numbers = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    result = num1 or num2
    return result, numbers


# generate lists of mathematical expressions and their answers
def get_gcd_lists():
    questions_gcd_list = []
    results_gcd_list = []
    for _ in range(3):
        result, numbers = get_gcd_result()
        questions_gcd_list.append(numbers)
        results_gcd_list.append(str(result))
    return questions_gcd_list, results_gcd_list


# run the create lists function pass its result to the
# variables that the engine imports
gcd_questions, gcd_results = get_gcd_lists()

# pack game variables in one for game engine
gcd = game_rule, gcd_questions, gcd_results
