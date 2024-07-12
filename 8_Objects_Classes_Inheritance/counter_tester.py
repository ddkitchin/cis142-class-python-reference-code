#imports from counter class
from Counter import Counter


def main() -> None:
    # 1 class Counter. 2 instance of class Counter costcoCounter and samsCounter
    costcoCounter = Counter()
    # If you don't have a dunder init __init__() you must reset in this class to get value set to 0.
    costcoCounter.reset()

    samsCounter = Counter()
    # If you don't have a dunder init __init__() you must reset in this class to get value set to 0.
    samsCounter.reset()

    while input("Continue?").upper() != "N":
        if input("Costco Customer?").upper() == "Y":
            costcoCounter.click()
        if input("Sams Customer?").upper() == "Y":
            samsCounter.click()

    print("Costco ", costcoCounter.getValue(), "Sams", samsCounter.getValue())


if __name__ == "__main__":
    main()
