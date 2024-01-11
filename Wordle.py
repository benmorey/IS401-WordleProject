# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    # Gets a FIVE_LETTER_WORD from WordleDictionary
    
    rand_word = random.randint(0, len(FIVE_LETTER_WORDS) - 1)
    print(rand_word)
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
