import random

print("Welcome to the number guessing game! ")

while True:
    try:
        upper_bound = int(input("Please choose the upperbound of your number: "))
        break
    except ValueError:
        print("Sorry, you have to enter a number instead of characters")


random = random.randint(1,upper_bound)
guesses = None
number_of_guess = 0

while random != guesses:
    while True:
        try:
            guesses = int(input(f"Please guess a random number between 1 and {upper_bound}: "))
            break
        except ValueError:
            print("Sorry, you will have to input numbers, not random character")

    if random == guesses:
        print(f"Fabulous, you got it!")
        number_of_guess += 1
    elif guesses > random:
        print("Slightly off by a bit, Please reduce the number ")
        number_of_guess += 1
    elif guesses < random:
        print("A bit too much, Please try a smaller number ")
        number_of_guess += 1
print(f"The random number is {random} and the total guesses you used were {number_of_guess}")






