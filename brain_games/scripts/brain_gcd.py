from brain_games.games.gcd_game import game_rule, gcd_questions, gcd_results
from brain_games.games_body import start_game


def main_gcd():
    start_game(game_rule, gcd_questions, gcd_results)


if __name__ == '__main__':
    main_gcd()
