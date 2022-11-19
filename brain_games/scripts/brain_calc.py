from brain_games.games.calc_game import game_rule, calc_questions, calc_results
from brain_games.games_body import start_game


def main_calc():
    start_game(game_rule, calc_questions, calc_results)


if __name__ == '__main__':
    main_calc()
