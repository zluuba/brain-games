from brain_games.games.progression_game import progression_game_rule, progression
from brain_games.games.body import welcome_user, user_name


def main():
    welcome_user()
    user_name()
    progression_game_rule()
    progression()


if __name__ == '__main__':
    main()
