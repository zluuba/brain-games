import prompt


ROUNDS = 3


def get_user_name_and_show_welcome(game_rule):
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May I have your name? ")
    print(f'Hello, {user_name}!')
    print(game_rule)
    return user_name


def get_user_answer_and_show_question(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def start_game(game):
    game_rule = game.game_rule
    user_name = get_user_name_and_show_welcome(game_rule)
    for _ in range(ROUNDS):
        correct_answer, question = game.get_result_and_question()
        user_answer = get_user_answer_and_show_question(question)
        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {user_name}!')
