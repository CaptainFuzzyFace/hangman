'''
Created on 16 Oct 2013

@author: j933346
'''
import sys
from words import Dict

def wordListLoad(fileName):
    '''
    Load the words from the file name given and return this as a list
    '''
    print("Building the word list...")

    word = ""
    level = 0
    fileLine = 0
    listOfWords = Dict()
    
    try:
        wordListFile = open(fileName,"r")
    except:
        print("Unable to open the file. No idea why.")
        return listOfWords
    
    try: 
        for wordLine in wordListFile:
            fileLine +=1
            seperatorIndex = wordLine.find(",")
            level = int(wordLine[seperatorIndex+1:])
            word = wordLine[:seperatorIndex]
            listOfWords.addWord(word, level)
        print("Words imported: " + str(fileLine))
    except:
        print("Problem loading the word list from: " + fileName)
        print("Please check that the file has valid contents, fix any problems and try again.")
        print(sys.exc_info())
    
    wordListFile.close()
    return listOfWords

def gameDifficulty(book):
    '''
    Select the level of the game
    0 = Quit
    +ve number, select that level if available
    Anything else, try again
    '''
    # Ask user for a difficulty level
    message = "\nPlease select a difficulty level. \n\n" + book.levelDescription(0) + "\n"
    validLevels = [True]
    for level in range(1,book.maxLevel()):
        validLevels.append(book.countWords(level) > 0)
        if validLevels[level]:
            message += "\n" + book.levelDescription(level) + "\n"
                
    level = -1
    while level < 0 :
        response = raw_input(message)
        try:
            level = int(response)
        except:
            level = -1
            
    return level

if __name__ == '__main__':
    
    # Build the word list
    wordBook = wordListLoad("C:\Users\J933346\workspace\Tutorial\mab\words.txt")
    
    # Ask which level to play at
    gameLevel = gameDifficulty(wordBook)
        
    # Start game
    chosenWord = wordBook.getWord(gameLevel)
    
    # Guesses left
    guessesRemaining = 13
    guessed = False
    quited = False 
    
    # Run the game
    lettersGuessed = ""
    while guessesRemaining > 0 and not (guessed or quited):
        # Draw hangman
        print(":-)<<<<<<<<<<<<"[0:guessesRemaining+3])
        # Draw word
        printable = ""
        guessed = True
        for letter in chosenWord:
            if letter in lettersGuessed: 
                printable += letter
            else:
                printable += "*"
                guessed = False

        if not guessed:
            # Draw letters guessed
            print("Today's word is: " + printable)
            print("You have guessed these letters already: " + lettersGuessed)
            # Accept guess
            letter = raw_input("Which letter would you like to guess next? ")
            quited = (letter == "")
            if not letter in lettersGuessed:
                lettersGuessed += letter.lower()

        # Good guess?
        if not letter in chosenWord:
            guessesRemaining -= 1
        
    if guessed:
        print("Congrats, you won! You correctly guessed " + chosenWord)
    else:
        print("Thanks for playing. The word was: " + chosenWord)
    
    # Quit the game
    
