from brain_games.games.even_game import game_rule, questions, results
from brain_games.games_body import start_game


def main_even():
    start_game(game_rule, questions, results)


if __name__ == '__main__':
    main_even()
