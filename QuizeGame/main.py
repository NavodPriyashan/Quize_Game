def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)

        guess = input("Enter (A, B, C, D): ").upper()
        while guess not in ['A', 'B', 'C', 'D']:
            print("Invalid input! Please enter A, B, C, or D.")
            guess = input("Enter (A, B, C, D): ").upper()

        guesses.append(guess)
        correct_guesses += check_answer(questions[key], guess)
        question_num += 1

    display_score(correct_guesses, guesses)
    play_again()


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!!")
        return 1
    else:
        print("Wrong!!")
        return 0


def display_score(correct_guesses, guesses):
    print("---------------------------------")
    print("RESULT")
    print("---------------------------------")

    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():
    play = input("Do you want to play again? (yes/no): ").lower()
    if play == 'yes':
        new_game()
    else:
        print("Thanks for playing!")


questions = {
    "Who created Python? :": "A",
    "What year was Python created? :": "B",
    "Python is tributed to which comedy group? :": "C",
    "Is Earth round? :": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smoch", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth"]
]

new_game()
