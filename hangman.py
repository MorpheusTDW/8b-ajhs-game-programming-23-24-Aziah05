# Hangman game by Aziah Hill, v0.0
import random
# words = 'chicken apple ugly nugget wild bad good something nothing want calm furious joy reveal blue purple yellow green red hot cold cool son mom dad uncle cousin aunt dry wet.'.split()
# DICTIONARY VERSION
# stored in key: value pairs.
# Actual Dictionary Word (Key) : Value (Definition)
# Uses {} to specify a dictionary
words = {'Colors': 'red orange yellow green blue indigo violet teal gold black white silver fushia'.split(),
        'Animals': 'cat cow dog moose goose fish wombat wolverine giraffe hippo lion alligator'.split(),
        'Shapes': 'square triangle rectangle circle rhombas parallelogram trapezoid diamond rectangle'.split(),
        'Food': 'hamburger hotdog potato waffle pancake eggs steak salmon donut'.split()}


# VARIABLE_NAMES in ALL CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |                 
        |
     =======''', '''
    +---+
    O   |
        |
        |
     =======''','''
     +---+
    O   |
    |   |
        |
     =======''','''
     +---+
    O   |
    |\  |
        |
     =======''','''
     +---+
    O   |
   /|\  |
        |
     =======''','''
     +---+
    O   |
   /|\  |
   /    |
     =======''','''
      +---+
    O   |
   /|\  |
   / \  |
     =======''','''
    +---+
    O   |
  o-|-o |
   / \  |
     =======''', '''
    +---+
    O   |
  o-|-o |
   / \  |
  o   o |
     =======''']

# Pick Word from list 
# def getRandomWord(wordList): # Return a random word from the list.
#    wordIndex = random.randint(0, len(wordList) - 1)
#    # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
#   return wordList[wordIndex]

# Pick word from dictionary
def getRandomWord(wordDict): # Return a random word from the list.
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey] 

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end =' ')
    print()
    
    blanks = '_' * len(secretWord)

    
    # Replace Blanks with Correct letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please pick a letter from A to Z and hit Enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('Letter has been guessed already, try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the English alphabet.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith('y')

# Introduce the Game
print('Welcome to Hangman by Aziah H')

# Choose Difficulty
difficulty = 'X'
while difficulty not in 'EMH':
    print('Please choose Easy, Medium or Hard. Type first letter then press enter.\n')
    difficulty = input().upper()
if difficulty == 'M': #Medium
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
if difficulty == 'H': #Hard
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[5]
    del HANGMAN_BOARD[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    print('The secret word is from the ' + secretSet + ' category.\n')
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check To see if winner, winner chicken dinner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:   # if True
                print('Much wow! Very Win! Well Done.')
                print('The secret word was' + secretWord)
                gameIsDone =True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have ran out of guess attempts and lost the game.')
            print('You have made this number of correct guesses ' + str(len(correctLetters)))
            print('The secret word was ' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break

# i = 0
# while i < 100:
#        word = getRandomWord(words)
#        print(word)
#        i += 1