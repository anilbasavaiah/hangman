import random
from optionslist import my_dict
import string

while True:
    def user_choice(name):
        word = random.choice(my_dict.get(name))
        return word.upper()
    try:
        user_input = input("Please select the name of the options to play - fruits or animals: ").lower()
    except KeyboardInterrupt as j:
        print("\nExiting the game")
        exit()


    def hangman():
        word = user_choice(user_input)
        word_letters = set(word)  # letters in the random word
        alphabet = set(string.ascii_uppercase)
        used_letters = set()  # user guessed words

        lives = 6
        # getting user input
        while len(word_letters) > 0 and lives > 0:
            # inform user about guessed letters
            print(f"You have left with {lives} lives and you have used letters: ", " ".join(used_letters))

            # what current word is (w _ r d)
            word_lst = [letter if letter in used_letters else "-" for letter in word]
            print("Current word", " ".join(word_lst))

            user_guess = input("Enter a letter ").upper()
            if user_guess in alphabet - used_letters:
                used_letters.add(user_guess)
                if user_guess in word_letters:
                    word_letters.remove(user_guess)
                else:
                    lives = lives - 1  # wrong answer looses a life
                    print("Letter is not in the word")

            elif user_guess in used_letters:
                print("You have already used the letter, please try again")

            else:
                print("Invalid character guessed, please try again")

        # gets here when the let(word_letters) == 0 or lives == 0
        if lives == 0:
            print(f"Sorry, you have lost all the lives, the word was {word}")
        else:
            print(f"You have guessed the word {word}")


    try:
        hangman()
    except NameError as e:
        print("Please select correct option")
    except TypeError as t:
        print("Please select correct option")
    except KeyboardInterrupt as k:
        print("\nExiting the game")
        exit()
