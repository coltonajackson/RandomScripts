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

answer = input("What is the word? ")
#hint_split = ["_" for c in answer]

guess = ""
guesses = 0
hint = ""
for char in answer:
        hint += "_"

while guess != answer:
    print("Your hint is:", hint)
    guess = input("What is your guess? ")
    if len(guess) == len(answer):
        guesses += 1
        new_hint = ""
        for char in enumerate(guess):
            if char[1] == answer[char[0]]:
                new_hint += char[1]
            else:
                new_hint += hint[char[0]]
        hint = new_hint
    else:
        print("Not a valid guess. Please guess again.")

print("\nCongratulations! You guessed it!")
print("It took you {0} guesses.".format(guesses))
