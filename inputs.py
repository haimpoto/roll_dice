def get_valid_num(massage: str, with_zero: bool = True) -> str:
    while True:
        user_input = input(massage)
        if not user_input.strip().isdigit():
            print("you need coise number!")
            continue
        elif (not with_zero) and (not int(user_input.strip())):
            print("0 is invalid!")
            continue
        break
    return user_input


def get_valid_string(massage: str) -> str:
    while True:
        user_input = input(massage)
        if not user_input.strip():
            continue
        break
    return user_input
       