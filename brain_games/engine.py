import prompt


def get_user_name_and_show_welcome(game_rule):
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game_rule)
    return name


def get_user_answer_and_show_question(expression):
    print(f'Question: {expression}')
    answer = prompt.string('Your answer: ')
    return answer


def is_correct(answer, result):
    if answer == result:
        return True
    else:
        return False


def start_game(game):
    game_rule = game.game_rule
    name = get_user_name_and_show_welcome(game_rule)
    rounds = 3
    for _ in range(rounds):
        result, expression = game.get_result_and_expression()
        answer = get_user_answer_and_show_question(expression)
        correct = is_correct(answer, str(result))
        if not correct:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
