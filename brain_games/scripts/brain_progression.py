from brain_games.games.progression_game import game_rule, questions, results
from brain_games.games_body import start_game


def main_progression():
    start_game(game_rule, questions, results)


if __name__ == '__main__':
    main_progression()
