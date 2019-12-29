#!/usr/bin/env python3

#Hang Man

from os import system, name
from time import sleep
import re

# Clears the console screen
def ClearScreen():
    #Windows
    if name == "nt":
        system("cls")
    #Linux
    else:
        system("clear")

def CreatePlaceholder(word, used_chars):
    guess = ""
    for w in word:
        if w in used_chars:
            guess += w.upper() + " "
        else:
            guess += '_ '
    
    return guess

def DrawHangman(guesses_counter):
    guesses_left = 6 - guesses_counter
    hangman = [ "O", "|", "/", "\\", "/", "\\" ]
    toDraw = """\t\t________
                |\t|
                {0}\t|
                {2}{1}{3}\t|
                {4}{5}\t|
                \t|
                \t|\n"""

    # Replace {#} above with corresponding hangman part or replace any leftover {#} above with empty string
    for x in range(0, 6):
        #print(toDraw.replace("{" + str(x) + "}", hangman[x]))
        toReplace = ""
        if x < guesses_left:
            toReplace = hangman[x]
        
        toDraw = toDraw.replace("{" + str(x) + "}", toReplace)   
    print(toDraw)
    
def main():
    ClearScreen()

    gameover = False
    used_chars = []
    word = "hangman"
    hint = "You must see the truth for yourself (i.e. you don't get one)"
    distinct_word = []
    guess_counter = 6

    # Get the word to guess: may only start/end with alphabetic letters or whitespace, and may not be more than 50 letters long
    while 1:
        word = input("Enter word to guess: ").lower()
        if not re.match("^[a-z ]*$", word) or len(word) > 50 or len(word) == 0:
            print("Error: You must enter letters a-z or spaces, and your word must be under 50 letters long!\n")
        else:
            break
    
    # if whitespace is in the word, treat it as a correct guess by the user
    if " " in word:
        used_chars.append(" ")

    # Let user enter a hint (or use defualt if none entered)
    temp_hint = input("Enter a hint (or not): ").strip()
    hint = temp_hint if len(temp_hint.strip()) > 0 else hint

    ClearScreen()

    # get all distinct letters of the word
    for w in word:
        if w not in distinct_word:
            distinct_word.append(w)
    distinct_word.sort()

    while gameover == False:
        print("Guess the word!\nYou can try {0} more times.\n".format(str(guess_counter)))
        print("Hint: " + hint + "\n")

        # Draw the hangman
        DrawHangman(guess_counter)

        # Create the placeholder string for correctly guessed letters so far
        print(CreatePlaceholder(word, used_chars) + "\n")

        # Check user input
        user_input = input("Guess a letter: ").lower()

        # Force input to be alphabetic only or whitespace, and to have length = 1
        if not re.match("[a-z]", user_input) or len(user_input) != 1:
            print("Error: Only letters a-z and spaces allowed!")
            input("Press ENTER to continue...")
            ClearScreen()
            continue

        # Show user-inputted letters already guessed
        if user_input not in used_chars:
            if user_input not in distinct_word:
                guess_counter -= 1
                print("'" + user_input + "' is wrong!")
            else:
                print("'" + user_input + "' is correct!")
            used_chars.append(user_input.lower())
        else:
            print("You already guessed '" + user_input + "'")
        
        print("Your guesses: " + ' '.join(x for x in sorted(used_chars)) + "\n")
        #print("Your guesses: " + ' '.join(x.replace(" ", "{space}") for x in sorted(used_chars)) + "\n")

        # Check if the user has guessed correctly
        correct_guesses = [] 
        for c in used_chars: # get all correct guesses so far
            if c in distinct_word:
                correct_guesses.append(c)

        # Compare the sorted word to the sorted guess
        if distinct_word == sorted(correct_guesses):
            ClearScreen()
            print("\n* CONGRATULATIONS! You guessed the word: '" + word + "' !*\n")
            gameover = True
        elif guess_counter <= 0:
            ClearScreen()
            print("\n* GAME OVER! The word was: '" + word + "' !*\n")
            gameover = True

        if gameover:
            DrawHangman(guess_counter)
            print(CreatePlaceholder(word, used_chars) + "\n")

        input("Press ENTER to continue...")
        ClearScreen()


        # print(distinct_word)
        # print("-----------------------------\n")
        # print(sorted(used_chars))


if __name__ == "__main__": 
    main()