# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR

# returns true if the input is a valid 5-letter english word
def is_english(word):
    return word.lower() in FIVE_LETTER_WORDS

def wordle():

    def enter_action(s):
        gw.show_message("Valid english word!" if is_english(s) else "Not in word list")
        
        # Tells the user when they guessed the right word
        if s == wordleWord:
            gw.show_message("That's correct! Nice job!")
        
        # Set CORRECT_COLOR
        for col in range (0, N_COLS):
            if s[col] == wordleWord[col]:
                gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
        
        # wordleWord copy that can be changed
        copyWordleWord = wordleWord
        # Set present color
        for col in range(0, N_COLS):
            # Check if letter color has already been filled out
            if gw.get_square_color(gw.get_current_row(), col) == UNKNOWN_COLOR:

                # FIX THIS FOR LOOP
                # This is where I'm starting to have issues. The problem is that most cases work, but currently if you enter a word that 
                # has two occurrences of a letter in the wordleWord both will be highlighted. 
                # I've set the wordleWord to be "HELLO" every time for debugging so to see what I'm talking about type in "SHOOT".
                # You'll see that both the "O"s highlight as yellow when only one of them should.

                # Iterate through the wordle word to see if the current letter is found in it.
                for wordleIndex in range(0, N_COLS):
                    # If the current letter is found then assign it PRESENT_COLOR
                    if s[col] == wordleWord[wordleIndex]: 
                        gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                        print(copyWordleWord)
                        break
        
        # NEXT STEP IS TO CHANGE THE ROW AFTER A USER ENTERS A GUESS

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # Choose random word from WordleDictionary.py
    displayWord = random.choice(FIVE_LETTER_WORDS)
    # Set first row characters to the characters from displayWord
    for col in range(0, N_COLS):
        gw.set_square_letter(0, col, displayWord[col].upper())

    # Sets the word the user is trying to guess!
    # wordleWord = random.choice(FIVE_LETTER_WORDS)
    wordleWord = "HELLO"
    
    guessNum = 0

# Startup code

if __name__ == "__main__":
    wordle()
