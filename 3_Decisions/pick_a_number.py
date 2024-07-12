#@copyright Deborah Kitchin

from random import randint


def main() -> None:
    number = randint(1, 10)

    # print(number) #Comment after testing done

    guess = 0
    count = 0

    while guess != number:
        guess = int(input("Guess a number "))
        count += 1
        if guess < number:
            print('The number is higher')
        elif guess > number:
            print('The number is lower')
        else:
            print(f'You guessed the number {guess} in {count} tries.')


if __name__ == "__main__":
    main()
