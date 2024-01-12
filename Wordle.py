# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

    #this function returns the word we just entered
def get_word(window):
    row = window.get_current_row()
    current_word = window.get_square_letter(row, 0) + window.get_square_letter(row, 1) + window.get_square_letter(row, 2) + window.get_square_letter(row, 3) + window.get_square_letter(row, 4)
    current_word = current_word.lower()
    return current_word


def wordle():
    gw = WordleGWindow()
    def enter_action(s):
        
        word = get_word(gw) #calls the get_word function
    
        if word in FIVE_LETTER_WORDS: #shows the user a message of whether or not their word is actually a word
            gw.show_message("This is a word! But are you right??? (Milestone 2)")
        else:
            gw.show_message("This is not a word!  (Milestone 2)")




    # # Gets a FIVE_LETTER_WORD from WordleDictionary
    # rand_num = random.randint(0, len(FIVE_LETTER_WORDS) - 1)
    # rand_word = FIVE_LETTER_WORDS[rand_num]

    # #Assigns the selected word to the boxes
    # for i in range(N_COLS):
    #     gw.set_square_letter(0, i, rand_word[i].upper())

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
