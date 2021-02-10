# imported random number generator to be used in our word selector
import random
from Holton_William_hangman_functions import get_letters_remaining

# Imported our word list that we will select our word from our text file 
import os
base_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(base_path, "word_list.txt")

with open(path, "r") as file:
    list_of_lines = file.readlines()

# created an empty list to fill with the extracted strings from the .txt file
wordlist = []
for line in list_of_lines:
    wordlist.append(line.replace("\n", ""))

# created a variable that will select a random word from our list
selected_word = wordlist[int(random.random() * len(wordlist))]


# created a guess limit
wrong_guess_limit = 7

# created a variable for the number of wrong guesses used
wrong_guesses = 0

# created a list to hold all our guesses and use to give feedback
previous_guesses = []

# Executed our get_letters_remaining function to display stars in place of letters
letters_remaining = get_letters_remaining(previous_guesses, selected_word)

# created a while loop to get guesses from user that will run as long as both conditions are met
while (wrong_guesses < wrong_guess_limit) and (letters_remaining != selected_word):

    # get user to guess a letter
    guess = input(f'{letters_remaining} \n Please enter your next guess: ').lower()

    # created a conditional to handle non alphabetical input 
    if guess.isalpha() == True:
        
        # Created a conditional to add to our wrong guess counter
        if guess in selected_word:
            pass
        else:
            wrong_guesses = wrong_guesses + 1

        # append the guess to the list of guesses and display to user
        previous_guesses.append(guess)

        # Use our imported function to return the letters remaining to guess
        letters_remaining = get_letters_remaining(previous_guesses, selected_word)

    else:
        print()
        print("YOU MUST GUESS A LETTER!")
        print()

# give feedback to the user to let them know if they've won or lost
if letters_remaining == selected_word:
    print('CONGRATULATIONS YOU WIN')
else:
    print('YOU LOSE')
