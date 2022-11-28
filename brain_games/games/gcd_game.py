from random import randint


game_rule = 'Find the greatest common divisor of given numbers.'


def get_numbers():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    return num1, num2


# find the greatest common divisor(gcd)
def get_result_and_expression():
    num1, num2 = get_numbers()
    expression = f'{num1} {num2}'

    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    result = num2
    return result, expression
