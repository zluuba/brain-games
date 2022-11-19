from brain_games.games.prime_game import game_rule, questions, results
from brain_games.games_body import start_game


def main_prime():
    start_game(game_rule, questions, results)


if __name__ == '__main__':
    main_prime()
