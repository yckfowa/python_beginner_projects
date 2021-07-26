import random

with open('words.txt') as words:
    secret_word = random.choice(words.readlines())
    secret_word = secret_word.rstrip("\n")

for index, char in enumerate(secret_word):
    if index == 0:
        print(f" {char.upper()}", end="")
    else:
        print(" _", end="")
print()

correct_letters = ""
wrong_inputs = 0
threshold = 5

while True:
    user_input = input("Please provide a letter or the solution: ")
    if len(user_input) > 1:
        if user_input.lower() != secret_word.lower():
            print(f"Game over, the secret word was '{secret_word}'")
            break
        else:
            print(f"Congrats!! The word is '{secret_word}'")
            break
    elif len(user_input) == 1:
        if user_input in secret_word:
            print(f"Correct, the letter '{user_input}' appears in the word!")
            correct_letters += user_input
        else:
            wrong_inputs += 1
            print(f"Wrong, the letter '{user_input}' does not appears in the word. Wrong inputs so far: {wrong_inputs} / {threshold}")

    if wrong_inputs >= threshold:
        print(f"You have provided {threshold} wrong answers. Game over! The word was '{secret_word}'.")
        break

    for index, char in enumerate(secret_word):
        if index == 0:
            print(f" {char.upper()}", end="")
        elif char in correct_letters:
            print(f" {char}", end="")
        else:
            print(" _", end="")
    print()
