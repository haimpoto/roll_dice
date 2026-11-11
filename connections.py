from pathlib import Path
import json

GAME_HISTORY_PATH = Path(__file__).parent / "game_history.json"


def load_game_history():
    try:
        with open(GAME_HISTORY_PATH, "r") as json_file:
            return json.load(json_file)
    except:
        return []


def save_game(data: dict) -> bool:
    with open(GAME_HISTORY_PATH, "r") as json_file:
        history = json.load(json_file)
    if not isinstance(history, list):
        return False
    history.append(data)
    with open(GAME_HISTORY_PATH, "w") as json_file:
        json.dump(history, json_file, indent=4)
    return True
