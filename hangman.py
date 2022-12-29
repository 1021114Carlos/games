#rules of the game: provide a secret word 
#that must be guessed by the participant.
#the participant can only miss a specified
#number of times.
#if word not quest correctly print the letters that were guessed
#correctly, if any, and dash where no word was guessed.

#---------------------------------

#pseudocode
#import libraries
#def guessed_word:
#is word guessed correctly return secret word
#otherwise return letters guessed, if any, and dashes 
#for place holders

#def letters_guessed:
#what is the secret word
#participant enters a letter
#if letter in secret word
#add letter to guessed_word
#if letter not in secret word
#mark as incorrect.

from string import *

secretWord=input("enter a word: ")
mistakesAllowed = 3
letters=[]
isWord_Guessed=False

def wordGuessed():
    
    
    def playerGuesses(sW):
        
        while isWord_Guessed:
            pass
            guess_Letter=input()

            for index, value in enumerate(sW):
                if value == guess_letter:
                    letters[index]=letters
                pass

            print(letters)

playerGuesses(secretWord)
