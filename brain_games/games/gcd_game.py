from random import randint


game_rule = 'gcd_game'


def get_gcd_result():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    numbers = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    pre_result = num1 + num2
    return pre_result, numbers


def get_gsd_lists():
    questions_gcd_list = []
    results_gcd_list = []
    for count in range(3):
        result, numbers = get_gcd_result()
        questions_gcd_list.append(numbers)
        results_gcd_list.append(str(result))
    return questions_gcd_list, results_gcd_list


questions, results = get_gsd_lists()
