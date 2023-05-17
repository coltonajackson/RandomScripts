print("Welcome to the word guessing game!")

print()
secret_word = "mosiah"
counter = 0
guess = ""
secret_word_length = len(secret_word)


def get_hint():
    hint_split = ["_" for c in secret_word]
    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            hint_split[i] = letter.upper()
        elif letter in secret_word:
            hint_split[i] = letter.lower()
        else:
            hint_split[i] = "_"
    return "".join(hint_split)


while guess != secret_word:
    print("Your hint is:", get_hint())
    guess = input("\nWhat is your guess? ")
    guess_length = len(guess)
    if guess_length != secret_word_length:
        print("Your guess is invalid. It will not count.")
    else:
        counter += 1

print("Congratulation!  You guessed it!")
# At this point, they guessed it correctly
print(f"It took you {counter} guesses")
