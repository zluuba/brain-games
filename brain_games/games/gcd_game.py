from random import randint
from brain_games.games_body import body


game_rule = 'gcd_game'


def get_gcd_result():
    global numbers
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    numbers = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    pre_result = num1 + num2
    return pre_result


def get_gsd_lists():
    questions_gcd_list = []
    results_gcd_list = []
    count = 0
    while count < 3:
        result = get_gcd_result()
        questions_gcd_list.append(numbers)
        results_gcd_list.append(str(result))
        count += 1
    return questions_gcd_list, results_gcd_list


def gcd_body():
    questions_gcd_list, results_gcd_list = get_gsd_lists()
    body(game_rule, questions_gcd_list, results_gcd_list)
