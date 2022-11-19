from brain_games.games.even_game import game_rule, even_questions, even_results
from brain_games.games_body import start_game


def main_even():
    start_game(game_rule, even_questions, even_results)


if __name__ == '__main__':
    main_even()
