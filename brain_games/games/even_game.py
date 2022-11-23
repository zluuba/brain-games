from random import randint


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


# creates one number and checks its parity
def get_num_and_result():
    num = randint(0, 25)
    result = 'yes' if num % 2 == 0 else 'no'
    return num, result


# generate lists of mathematical expressions and their answers
def get_even_lists():
    questions_even_list = []
    results_even_list = []
    for _ in range(3):
        num, result = get_num_and_result()
        questions_even_list.append(num)
        results_even_list.append(str(result))
    return questions_even_list, results_even_list


# run the create lists function pass its result to the
# variables that the engine imports
even_questions, even_results = get_even_lists()

# pack game variables in one for game engine
even = game_rule, even_questions, even_results
