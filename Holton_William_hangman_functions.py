
def get_letters_remaining(previous_guesses, selected_word):

    #create a for loop to correctly display the letters and asterisks in the same place

    letters_remaining = ''
    for letter in selected_word:
        # we assign boolean true value to each letter to begin with
        
        add_asterisk = True 
        add_letter = False
        
        for guess in previous_guesses:

            if guess == letter:
                # we will assign a boolean false to the letter if the guess is correct
                add_asterisk = False 
                add_letter = True
        
        # there will be an asterisk placed in place of a letter if the letter is still
        # holding a true value.
        if add_asterisk == True:
            letters_remaining = letters_remaining + '*'

        # if the letter value has been switched to false by our for loop the letter will be shown
        if add_letter == True:
            letters_remaining = letters_remaining + letter 



    return letters_remaining


    print(letters_remaining) 
