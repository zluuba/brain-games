import prompt


def welcome_user(rule):
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    rule()


def question(expression):
    print(f'Question: {expression}')
    return prompt.string('Your answer: ')


def is_correct(answer, result):
    if answer == result:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        return False


def win():
    print(f'Congratulations, {name}!')


def lose():
    print(f"Let's try again, {name}!")


def game_body(rule, expressions, results):
    welcome_user(rule)
    count = 0
    while count < 3:
        answer = question(expressions[count])
        result = str(results[count])
        correct = is_correct(answer, result)
        if correct:
            count += 1
            continue
        else:
            lose()
            break
    else:
        win()
