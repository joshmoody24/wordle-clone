# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

# returns true if the input is a valid 5-letter english word
def is_english(word):
    return word.lower() in FIVE_LETTER_WORDS

def wordle():

    def enter_action(s):
        gw.show_message("Valid english word!" if is_english(s) else "Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
