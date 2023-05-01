import random
import os
from words import word_list
from graphics import stages


def choose_mode():
    choice = input("\nType '1' for single-player or '2' for multiplayer: ")
    if choice not in ["1", "2"]:
        print(f"\nInvalid input.")
        choose_mode()
    else:
        return choice

def choose_word():
    choice = input(f"\nPlayer 2, please look away.\nPlayer 1, please input a word: ").lower()
    if choice.isalpha() == False:
        print(f"\nInvalid input. Please enter a single word with no spaces, numbers, or special characters.")
        choose_word()
    else:
        return choice

mode = choose_mode()

if mode == "1":
    chosen_word = random.choice(word_list)
else:
    chosen_word = choose_word()

display = []
wrong_guesses = []
for character in chosen_word:
    display.append("_")
lives = 6

os.system('clear')

if mode == "2":
    print("Player 1, start game.")
else:
    print("Start game.")

while ("_" in display) and (lives > 0):
    print(f"\nProgress: {' '.join(display)}")
    if len(wrong_guesses) > 0:
        print(f"Previous wrong guesses: {', '.join(wrong_guesses)}.\n{lives} guesses remaining.")
    else:
        print("No wrong guesses yet.\n6 guesses remaining.")
    print(stages[lives])
    guess = input("\nGuess a letter: ").lower()
    if guess in display or guess in wrong_guesses:
        os.system('clear')
        print(f"The letter '{guess}' has already been guessed.")
    elif len(guess) > 1:
        os.system('clear')
        print("Please enter just one letter.")
    else:
        if guess.isalpha() == False:
            os.system('clear')
            print("Invalid input. Please enter a letter.")
        else:
            if guess not in chosen_word:
                lives -= 1
                wrong_guesses.append(guess)
                os.system('clear')
                print(f"Incorrect. '{guess}' is not part of the word.")
            else:    
                for i in range(0, len(chosen_word)):
                    if chosen_word[i] == guess:
                        display[i] = guess
                os.system('clear')
                print(f"Correct - '{guess}' is part of the word.")

print(stages[lives])
if lives > 0:
    print(f"You win.\nWord was: {chosen_word}")
else:
    print(f"You lose.\nWord was: {chosen_word}\n")