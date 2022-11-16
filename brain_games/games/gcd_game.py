from random import randint
from brain_games.body import welcome_user, question, is_correct, lose, win


def gcd_rule():
    print('Find the greatest common divisor of given numbers.')


def gcd_welcome():
    welcome_user()
    gcd_rule()


def get_result():
    global expression
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    expression = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    pre_result = num1 + num2
    return pre_result


def greatest_cd():
    count = 0
    while count < 3:
        result = str(get_result())
        answer = question(expression)
        correct = is_correct(answer, result)
        if correct:
            count += 1
            continue
        else:
            lose()
            break
    else:
        win()
