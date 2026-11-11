def print_main_menu() -> None:
    print("""
================================
          ROLL DICE
================================

1. Start New Game
2. View Game History
3. View Statistics
4. Exit
"""
)   
    return

def print_new_game() -> None:
    print("""
================================
          NEW GAME
================================
"""
)
    return


def print_game_deta(player_name: str, number_of_rounds: int) -> None:
    print(f"""Player name: {player_name}
Number of rounds: {number_of_rounds}
""")
    return


def print_round_res(round_res: dict[str, int], user_name: str) -> None:
    print(f"""{user_name}:\t\t🎲 {round_res["user_roll"]}
Computer:\t🎲 {round_res["computer_roll"]}
""")


def print_winner(winner: str, user_name: str) -> None:
    if winner == "draw":
        print("draw")
        return
    print(f"{user_name if winner == "user" else winner} wins this round!")


def display_game_history(game_history: list) -> None:
    if not game_history:
        print("No game history")
        return
    for game in game_history:
        print(f"""player_name: {game["player_name"]}
rounds: {game["rounds"]}
player_score: {game["player_score"]}
computer_score: {game["computer_score"]}
winner: {game["winner"]}
""")
