import prompt


num_of_rounds = 3


def get_user_name_and_welcome_him(game_rule):
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game_rule)
    return name


def get_user_answer_and_show_question(expression):
    print(f'Question: {expression}')
    answer = prompt.string('Your answer: ')
    return answer


def is_correct_check_and_show_to_user(answer, result):
    if answer == result:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        return False


def show_user_win(name):
    print(f'Congratulations, {name}!')


def show_user_lose(name):
    print(f"Let's try again, {name}!")


def start_game(game):
    game_rule, expressions, results = game
    name = get_user_name_and_welcome_him(game_rule)
    for round in range(num_of_rounds):
        answer = get_user_answer_and_show_question(expressions[round])
        result = str(results[round])
        correct = is_correct_check_and_show_to_user(answer, result)
        if not correct:
            show_user_lose(name)
            break
    else:
        show_user_win(name)
