from Questions import Question, ChoiceQuestion


def main() -> None:
    first = Question()
    first.setText("Who was the inventor of Python?")
    first.setAnswer("Guido van Rossum")

    second = ChoiceQuestion()
    second.setText("In which country was the inventor of Python born?")
    second.addChoice("Australia", False)
    second.addChoice("Canada", False)
    second.addChoice("Netherlands", True)
    second.addChoice("United States", False)

    presentQuestion(first)
    presentQuestion(second)


def presentQuestion(q: Question) -> None:
    q.display()  # Uses dynamic method lookup.
    response = input("Your answer: ")
    if q.checkAnswer(response):  # checkAnswer uses dynamic method lookup.
        print(f'Congratulations you got the right answer')
    else:
        print(f'I am sorry. That is not the correct answer')
    print()


if __name__ == "__main__":
    main()
