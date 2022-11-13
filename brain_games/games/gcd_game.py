from random import randint
import prompt


def welcome():
    print('Welcome to the Brain Games!')


def user_name():
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def gcd_question():
    result = ''
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    print(num1, num2)
    global answer
    answer = prompt.string('Your answer: ')

    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
        result = num1 + num2
    return result


def greatest_cd():
    name = user_name()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        result = str(gcd_question())
        if answer == result:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
