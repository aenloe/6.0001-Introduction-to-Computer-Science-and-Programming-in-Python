# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


#Three helper Functions originally outlined by problem set. 

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    counter = 0
    for x in secret_word:
        
        for y in letters_guessed:
            if x == y:
                counter = counter + 1
                break
            else:
                continue
        
    if counter == len(secret_word):
        return True
    else:
        return False
     
     

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for x in secret_word:
        
        counter = 0
        for y in letters_guessed:
            
            if x == y:
                guessed_word.append(y)
                break
            else:
                counter = counter + 1
                if counter == len(letters_guessed):
                    guessed_word.append("_ ")
                else:
                    pass
            

    concatenated_list = "".join(guessed_word)
    return concatenated_list



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet_list = list(string.ascii_lowercase)
    for x in letters_guessed:
        
        for y in alphabet_list:
            if x == y:
                alphabet_list.remove(y)
                break
            else:
                continue
    
    modified_alphabet_list = "".join(alphabet_list)
    return modified_alphabet_list

#--------------------------------

#Three self designed functions to help with nested guessed_feedback function.

def check_input_is_letter(guessed_input):
    '''
    Create list of uppercase/lowercase letters to compare input value against. 
    If input match elements in list, return True. False otherwise.
    '''
    list_of_valid_values = list(string.ascii_letters)
    for x in list_of_valid_values:
        if guessed_input == x:
            return True
        else:
            continue
    return False

def check_input_is_repeat(guessed_input, letters_guessed):
    '''
    Sort through letters_guessed list to see if input matches.
    Return True if letter was already guessed. False otherwise.
    '''
    for x in letters_guessed:
        if x == guessed_input:
            return True
        else:
            continue
    return False

def check_consonant_vowel(guessed_input, secret_word):
    '''
    Sort through secret_word to see if input matches.
    Return 0 if match, 1 if no match + consonant, 2 if no match + vowel
    '''
    consonant_list = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    vowel_list = ["a","e","i","o","u"]
    for x in secret_word:
        if guessed_input == x:
            return 0
    
    for x in vowel_list:
        if guessed_input == x:
            return 2
        else:
            continue
        
    for x in consonant_list:
        if guessed_input == x:
            return 1
        else:
            continue


#-------------------------------------
        

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed. 
      "get_available_letters"
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter! 
      "check_input_is_letter"
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
      "guess_feedback" - nested function

    * After each guess, you should display to the user the 
      partially guessed word so far. 
      "get_guessed_word"
    
    Follows the other limitations detailed in the problem write-up.
    '''
    def guess_feedback():
        '''Main code block in hangman placed into a nested function for easier reading'''
        nonlocal guesses_remaining
        nonlocal warnings_remaining
        nonlocal letters_guessed
        
        #First, check if input is valid.
        if check_input_is_letter(guessed_input) == False:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid input. You have " + str(warnings_remaining) + " warnings left: "
                      + get_guessed_word(secret_word, letters_guessed))
                return
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid input. You have no more warnings left so you lose one guess: "
                      + get_guessed_word(secret_word, letters_guessed))
                return

        #Second, check if input is a repeat.
        elif check_input_is_repeat(guessed_input, letters_guessed) == True:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have " 
                      + str(warnings_remaining) + " warnings left: "
                      + get_guessed_word(secret_word, letters_guessed))
                return
            else:
                print("Oops! That is not a valid input. You have no more warnings left so you lose one guess: "
                      + get_guessed_word(secret_word, letters_guessed))
                return
        #Third, if input is valid and passes above checks, give result from correct/incorrect letter
        elif check_consonant_vowel(guessed_input, secret_word) == 0:
            letters_guessed.append(guessed_input)
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            return
        elif check_consonant_vowel(guessed_input, secret_word) == 1:
            guesses_remaining -= 1
            letters_guessed.append(guessed_input)
            print("Oops! That consonant is not in my word, you lose one guess: "
                  + get_guessed_word(secret_word, letters_guessed))
            return
        elif check_consonant_vowel(guessed_input, secret_word) == 2:
            guesses_remaining -= 2
            letters_guessed.append(guessed_input)
            print("Oops! That vowel is not in my word, you lose two guesses: "
                  + get_guessed_word(secret_word, letters_guessed))
            return
            
    #Variables
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    
    #Introduction
    print("Welcome to the game: Hangman!")
    print("I'm thinking of a word that is " + str((len(secret_word))) + " letters long.")
    print("You have " + str(warnings_remaining) + " warnings and " + str(guesses_remaining) + " guesses left.")
    print("Available letters: " + get_available_letters(letters_guessed))
    print("--------------------------")
    
    #Main loop
    while guesses_remaining > 0:
        print("You have " + str(warnings_remaining) + " warnings and " + str(guesses_remaining) + " guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        
        guessed_input = input(f"Please guess a letter: ")
        guess_feedback()

        print("--------------------------")
        
        if is_word_guessed(secret_word, letters_guessed) == True:
            break
    
    #Post-game score code
    def get_score(guesses_remaining, secret_word):
        '''
        returns score from a winning game in string format. 
        Score = guesses_remaining*number of unique letters in secret_word
        '''
        uniques = []
        for e in secret_word:
            for e1 in uniques[:]:
                if e == e1:
                    break
            uniques.append(e)
        return(str(guesses_remaining*(len(uniques))))
    
    if guesses_remaining <= 0:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
    else:
        print("Congratulations, you won!")
        print("Your total score for this game is: " + get_score(guesses_remaining, secret_word))

        
        
#hangman(secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def remove_spaces(x):
    '''
    iterate through string x, build list of index values for those that are spaces
    reverse read index list and remove spaces working backwards on string    
    returns: string without spaces
    '''
    #check for spaces, create index list
    spaces_list = []
    y = 0
    for e in x:
        if e == ' ':
            spaces_list.append(y)
        y += 1
    
    #modify string based on index
    for e in spaces_list[::-1]:
        if e == 0:
            x = x[e+1:]
            break
        x = x[:e] + x[e+1:]
    return x

def match_underscore(S1, S2):
    '''
    compare strings S1 to S2, skip underscores
    return: True if S1 == S2, False otherwise
    '''
    if len(S1) != len(S2):
        return False
    
    i = 0
    for x in S1:
        
        if x == "_":
            i += 1
            continue
        
        elif S2[i] != x:
            return False
        i += 1

    return True

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    #my_word is effectively the return output of get_guessed_word
    my_word = remove_spaces(my_word)
    return match_underscore(my_word, other_word)
    


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    words_that_match = []
    
    
    print(words_that_match)
    return None



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
