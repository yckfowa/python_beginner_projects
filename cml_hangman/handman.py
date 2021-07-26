import random


def get_word():
    with open("words.txt") as word_list:
        return random.choice(word_list.readlines()).rstrip("\n")


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("It's Hangman Time!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess letter or word: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is the word!.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word, {guess}")
            elif guess != word:
                print(f"{guess}, is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess. try again in alphabet")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word, You win!")
    else:
        print(f"Sorry , you ran out of tries. The word was {word}, Better luck next time ")


def display_hangman(tries):
    stages = [

                """
                    ------------
                    |          |
                    |          @
                    |         -|-
                    |         / \\
                    |
    
                """,

                """
                    ------------
                    |          |
                    |          @
                    |         -|-
                    |         / 
                    |
    
                """,


                """
                    ------------
                    |          |
                    |          @
                    |         -|-
                    |         
                    |

                """,


                """
                    ------------
                    |          |
                    |          @
                    |         -|
                    |         
                    |

            
                """,


                """
                    ------------
                    |          |
                    |          @
                    |          |
                    |         
                    |
                
                
                """,


                """
                    ------------
                    |          |
                    |          @
                    |          
                    |         
                    |
                
                """,



                """
                    ------------
                    |          |
                    |          
                    |          
                    |         
                    |
            
                """

    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N)").upper == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
