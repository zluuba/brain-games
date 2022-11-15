from brain_games.games.progression_game import game_rule, progression
from brain_games.games.body import welcome_user, user_name


def progression_game():
    game_rule()
    progression()


def main():
    welcome_user()
    user_name()
    progression_game()


if __name__ == '__main__':
    main()
