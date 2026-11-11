import connections
import game_logic
import inputs
import prints


def main() -> None:
    while True:
        prints.print_main_menu()
        user_choice = inputs.get_valid_num("Choose an option: ", with_zero=False)
        if user_choice == "1":
            game_logic.start_game()
        elif user_choice == "2":
            prints.display_game_history(connections.load_game_history())
        elif user_choice == "3":
            pass
        elif user_choice == "4":
            break
        else:
            print("inalid choise!")



if __name__ == "__main__":
    main()
