print("\n")
print("Welcome to my word guessing game!")
print("You have 3 guesses, have fun!\n")
print("Your hint is: appliances\n")

secret_word = "stove"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
    if guess_count == 2:
        guess = input("This is your last chance: ")
        guess_count += 1


if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("Congratulations!")


