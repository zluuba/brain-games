from brain_games.games.prime_game import prime_game_rule, prime_game
from brain_games.games.body import welcome_user, user_name


def main():
    welcome_user()
    user_name()
    prime_game_rule()
    prime_game()


if __name__ == '__main__':
    main()
