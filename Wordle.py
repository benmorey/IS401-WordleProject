# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR, KEY_COLOR

global gameNum

    #this function returns the word we just entered
def get_word(window):
    row = window.get_current_row()
    current_word = window.get_square_letter(row, 0) + window.get_square_letter(row, 1) + window.get_square_letter(row, 2) + window.get_square_letter(row, 3) + window.get_square_letter(row, 4)
    current_word = current_word.lower()
    return current_word, row

def wordle():
    CORRECT_VARIABLE = CORRECT_COLOR
    PRESENT_VARIABLE = PRESENT_COLOR
    name = input("\nWhat's your name: ")
    color_scheme = input("Do you want to use high contrast mode? (y/n) ")
    if color_scheme == "y":
        CORRECT_VARIABLE = "#FFA500"
        PRESENT_VARIABLE = "#0000FF"
    else:
        CORRECT_VARIABLE = CORRECT_COLOR
        PRESENT_VARIABLE = PRESENT_COLOR
    #this code pulls the actual word at the start of the game
    gameNum = 1
    wordArray = []
    booleanArray = [False, False, False, False, False]
    actual_word = FIVE_LETTER_WORDS[random.randint(1,len(FIVE_LETTER_WORDS))]
    for letter in actual_word:
        wordArray.append(letter)
    
    # 
    gw = WordleGWindow()
    
    def enter_action(s):
        outputArray = []
        shareOutput = ""
        row = 0
        word, row = get_word(gw) #calls the get_word function
        if word in FIVE_LETTER_WORDS: #shows the user a message of whether or not their word is actually a word
            #gw.show_message("This is a word! But are you right???")
            #loop to check for green letters
            guessWord = []
            for x in word:
                guessWord.append(x)
                
            #iterates through the entire guessword
            for i in range(0,5):
                if wordArray[i] == guessWord[i]:
                    gw.set_square_color(row, i, CORRECT_VARIABLE)
                    gw.set_key_color(gw.get_square_letter(row, i), CORRECT_VARIABLE)
                    booleanArray[i] = True
                       
                    
            #loop to check for tan letters
            for i in range(0,5):
                for j in range(0,5):
                    if wordArray[i] == guessWord[j] and gw.get_square_color(row,j) != CORRECT_VARIABLE and booleanArray[i] == False:
                        gw.set_square_color(row, j, PRESENT_VARIABLE)
                        # Check the keyboard color to see if it's correct or not
                        if gw.get_key_color(gw.get_square_letter(row, j)) != CORRECT_VARIABLE:
                            gw.set_key_color(gw.get_square_letter(row, j), PRESENT_VARIABLE)
                        booleanArray[i] = True
                        # guessWord[j] = '-'



        else:
            gw.show_message("This is not a word!  Try again!")
            #trying to create functionality for when the

        for i in range(0,6):
            for j in range(0,5):
                if gw.get_square_color(i,j) == CORRECT_VARIABLE:
                    shareOutput = shareOutput + "🟩"
                elif gw.get_square_color(i,j) == PRESENT_VARIABLE:
                    shareOutput = shareOutput + "🟨"
                else:
                    shareOutput = shareOutput + "⬛"
            outputArray.append(shareOutput)
            shareOutput = ''

        # End of game Functionality
        if booleanArray == [True,True,True,True,True]:
            
            print("\n" + name + "'s Wordle Stats: " + str(row + 1) + "/6\n\n")
            for i in range(0,row+1):
                print(outputArray[i])

        for i in range(0,5):
            booleanArray[i] = False    

        row = row + 1
        if(row == 6):
            gw.show_message("We're sorry, but the word was: " + actual_word)
            print("\n" + name + "'s Wordle Stats: " + str(row) + "/6\n\n")
            for i in range(0,row+1):
                if (i == 6):
                    continue
                else:
                    print(outputArray[i])
        else:
            gw.set_current_row(row)

        print("\n")
           
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
