import random


def zagadannoe_num():
    return random.randint(1, 101)


def zadacha():
    num = zagadannoe_num()
    res = 0
    while res != 10:
        try:
            vvod = int(input())
        except ValueError:
            print('Надо ввести число!')
        else:
            if vvod > num:
                print("Загаданное число меньше!")
                res += 1
                continue
            elif vvod < num:
                print("Загаданное число больше!")
                res += 1
                continue
            else:
                print(f"Поздравляем! Вы угадали число за {res} попыток!")
                break
    print(f"К сожалению, вы не угадали число. Загаданное число было {num}.")


if __name__ == '__main__':
    zadacha()