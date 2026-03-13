import random


def main():
    n = level_check()
    program_x = random.randint(1, n)

    while True:
        x = guess_check()
        if x < program_x:
            print("Too small")
        elif x > program_x:
            print("Too large")
        else:
            print("Just right")
            break


def level_check():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                raise ValueError
            else:
                return n
        except ValueError:
            continue


def guess_check():
    while True:
        try:
            x = int(input("Guess: "))
            if x <= 0:
                raise ValueError
            else:
                return x
        except ValueError:
            continue


main()
