import inputs
import random
import prints
import connections


GAME_STATS_EXAMPLE = { 
    "player_name": "",
    "rounds": 0,
    "player_score": 0,
    "computer_score": 0,
    "winner": "",
    "results": []}


def roll_dice() -> int:
    return random.randint(1, 6)


def play_round() -> dict[str, int]:
    input("Press enter to roll the dice")
    user_roll = roll_dice()
    computer_roll = roll_dice()
    return {"user_roll": user_roll,
    "computer_roll": computer_roll}


def calculate_round_winner(round_result: dict[str, int]) -> str:
    if round_result["user_roll"] > round_result["computer_roll"]:
        return "user"
    elif round_result["computer_roll"] > round_result["user_roll"]:
        return "computer"
    else:
        return "draw"


def calculate_winner(game_stats, user_name) -> str:
    if game_stats["player_score"] > game_stats["computer_score"]:
        return user_name
    elif game_stats["computer_score"] > game_stats["player_score"]:
        return "computer"
    else:
        return "draw"


def update_round_winner(game_stats, winner):
    if winner == "user":
        game_stats["player_score"] += 1
    elif winner == "computer":
        game_stats["computer_score"] += 1


def start_game():
    player_name = inputs.get_valid_string("Enter your name: ")
    number_of_rounds = int(inputs.get_valid_num("Chose number of rounds: ", with_zero=False))
    game_stats = {"player_score": 0, "computer_score": 0,}
    game_stats["player_name"] = player_name
    game_stats["rounds"] = number_of_rounds
    game_stats["results"] = []
    while number_of_rounds > 10:
        print("Enter number beteen 1 - 10")
        number_of_rounds = int(inputs.get_valid_num("Chose number of rounds: ", with_zero=False))
    prints.print_new_game()
    prints.print_game_deta(player_name, number_of_rounds)
    for i in range(number_of_rounds):
        print(f"---------- ROUND {i+1} ----------")
        res_of_round = play_round()
        prints.print_round_res(res_of_round, player_name)
        round_winner = calculate_round_winner(res_of_round)
        update_round_winner(game_stats, round_winner)
        prints.print_winner(round_winner, player_name)
        game_stats["results"].append(
            {"round": i + 1,
            "player_dice": res_of_round["user_roll"],
            "computer_dice": res_of_round["computer_roll"],
            "winner": round_winner}
            )
    game_stats["winner"] = calculate_winner(game_stats, player_name)
    print(f"\nWINNER: {game_stats["winner"]}!")
    save_success = connections.save_game(game_stats)
    if not save_success:
        print("error: the game is not saved.")

