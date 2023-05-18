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

import random

random_words = ["phone", "flowers", "towel", "laptop", "mother", "sealing", "book"]

print("Welcome to the word guessing game!\n")

answer = random.choice(random_words)

guess = ""
guesses = 0
hint = "_" * len(answer)

while guess != answer:
    print("Your hint is:", hint)
    hint = str.lower(hint)
    guess = input("What is your guess? ")
    if len(guess) == len(answer):
        guesses += 1
        new_hint = ""
        for char in enumerate(guess):
            if char[1] == answer[char[0]] and char[1] != hint[char[0]]:
                new_hint += str.upper(char[1])
            else:
                new_hint += hint[char[0]]
        hint = new_hint
    else:
        print(
            "Sorry, the guess must have the same number of letters as the secret word."
        )

print("\nCongratulations! You guessed it!")
print("It took you {0} guesses.".format(guesses))
