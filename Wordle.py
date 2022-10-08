# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR

# Milestone 1 Function
def set_first_row_random(gw):
    # Choose random word from WordleDictionary.py
    randomWord = random.choice(FIVE_LETTER_WORDS)
    # Set first row characters to the characters from randomWord
    for col in range(0, N_COLS):
        gw.set_square_letter(0, col, randomWord[col].upper())

def is_english(word):
    return word.lower() in FIVE_LETTER_WORDS

def colorize_current_row(guess, answer, gw):
    # this dictionary tracks the number of times each letter appears in the answer
    word_counts = {}
    for col in range(N_COLS):
        letter = answer[col]
        if(letter not in word_counts):
            word_counts[letter] = 1
        else:
            word_counts[letter] += 1

    # set them all to unknown color to start (just in case
    for col in range(N_COLS):
        gw.set_square_color(gw.get_current_row(), col, UNKNOWN_COLOR)
    
    # Turn exactly correct guesses green
    for col in range (N_COLS):
        guess_letter = guess[col]
        if(guess_letter == answer[col] and word_counts[guess_letter] > 0):
            gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
            word_counts[guess_letter] -= 1

    # Turn near misses yellow
    for col in range(N_COLS):
        guess_letter = guess[col]
        if(guess_letter in answer and word_counts[guess_letter] > 0 and (gw.get_square_color(gw.get_current_row(), col) == UNKNOWN_COLOR)):
            gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
            word_counts[guess_letter] -= 1

def colorize_keyboard(guess, answer, gw):
    
    # Set keys to green, yellow, or grey depending on if they are correct
    for col in range (N_COLS):
        guess_letter = guess[col]
        # Set to yellow if the letter is in the word.
        # If the letter is already green, don't change it to yellow again.
        if(guess_letter in answer and gw.get_key_color(guess_letter.upper()) != CORRECT_COLOR):
            gw.set_key_color(guess_letter.upper(), PRESENT_COLOR)
        # Set to green if correctly guessed
        if(guess_letter == answer[col]):
            gw.set_key_color(guess_letter.upper(), CORRECT_COLOR)
        # Set to dark grey if not in word
        if not(guess_letter in answer):
            gw.set_key_color(guess_letter.upper(), MISSING_COLOR)

def wordle():

    gw = WordleGWindow()
    # answer = "HELLO"
    answer = random.choice(FIVE_LETTER_WORDS).upper()
    print(answer)

    # set_first_row_random(gw)
    
    def enter_action(guess):
        if(" " in guess):
            return
        if(not is_english(guess)):
            gw.show_message("Not in word list")
            return
        colorize_current_row(guess, answer, gw)
        colorize_keyboard(guess, answer, gw)
        # Tells the user when they guessed the right word
        if guess == answer:
            gw.show_message("That's correct! Nice job!")
        
        gw.set_current_row(gw.get_current_row() + 1)
    
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()
