import random

MIN_RANGE: int = 1
MAX_RANGE: int = 100


def get_random_num(start: int, end: int) -> int:
    return random.randint(start, end + 1)


def is_validate(num: int) -> bool:
    if not (MIN_RANGE <= num <= MAX_RANGE):
        print(
            "Загаданное число находится в диапазоне "
            f"от {MIN_RANGE} до {MAX_RANGE}"
        )
        return False
    return True


def game_logic(user_num: int, guess: int) -> str:
    if user_num > guess:
        return "Загаданное число меньше!"
    elif user_num < guess:
        return "Загаданное число больше!"


def main() -> None:
    guess: int = get_random_num(MIN_RANGE, MAX_RANGE)

    print(
        "Загаданное число находится в диапазоне "
        f"от {MIN_RANGE} до {MAX_RANGE}"
    )

    attempt: int = 0
    while attempt < 3:
        try:
            user_num: int = int(input())
        except ValueError:
            print('Надо ввести целое число!')
        else:
            if user_num == guess:
                print(
                    "Поздравляем! Вы угадали число "
                    f"за {attempt} попыток!"
                )
                break
            if is_validate(user_num):
                print(game_logic(user_num, guess))
        attempt += MIN_RANGE
    else:
        print("К сожалению, вы не угадали число. "
              f"Загаданное число было {guess}.")


if __name__ == "__main__":
    main()
