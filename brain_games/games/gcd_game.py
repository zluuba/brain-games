from random import randint


game_rule = 'Find the greatest common divisor of given numbers.'


def get_result_and_question():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    question = f'{num1} {num2}'
    result = get_gcd(num1, num2)
    return result, question


def get_gcd(num1, num2):
    """
    Find the greatest common divisor(gcd)
    using Repeated Subtraction.
    """
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num2
