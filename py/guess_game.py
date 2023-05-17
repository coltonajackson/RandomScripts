"""
Example results:
Welcome to the word guessing game!

Your hint is: ______
What is your guess? temple
Your hint is: ______
What is your guess? moroni
Your hint is: mo____
What is your guess? mosiah

Congratulations! You guessed it!
It took you 3 guesses.
"""

print("Welcome to the word guessing game!\n")

answer = "mosiah"
hint_split = ["_" for c in answer]

guess = ""
guesses = []

while guess != answer:
    hint = "".join([c for c in hint_split])
    print("Your hint is:", hint)
    guess = input("What is your guess? ")
    guess_split = list(guess)
    answer_split = list(answer)
    if len(guess_split) == len(answer_split):
        guesses.append(guess)
        for idx, char in enumerate(guess):
            if guess_split[idx] == answer_split[idx]:
                hint_split[idx] = guess_split[idx]
                hint = "".join([c for c in hint_split])
    else:
        print("Not a valid guess. Please guess again.")

print("\nCongratulations! You guessed it!")
print("It took you {0} guesses.".format(len(guesses)))
