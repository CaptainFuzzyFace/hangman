#
#   Created on 16 Oct 2013
#
#   @author: j933346
#
from random import randint
import itertools

class Dict(object):
    # Managaging the word list used in hangman
    
    def __init__(self):
        # Constructor
        
        self._maxLevel = 6
        self._wordList = []
        self._wordCount = []
        for level in range(0,self._maxLevel):
            self._wordList.append([])
            self._wordCount.append(0)
        self.addWord("Quit",0)
        self._levelDescription = ("0. Quit"
                                  ,"1. Simple, short and solvable"
                                  ,"2. Nothing too challenging here"
                                  ,"3. Turns the brain on but won't wear it out"
                                  ,"4. Hopefully will make your brain warm up"
                                  ,"5. Tricky words that you probably don't use for months at a time"
                                  ,"6. Words that you may not even have heard of")

    # @Words.setter
    def addWord(self, word, level):
        # Add a new word to the list of available words. Requires a level too

        # TODO: Does this work? Do I need to pad the empty slots in the list? 
        self._wordList[level].append(word)
        self._wordCount[level] += 1
    
    def getWord(self, level):
        '''
        Get a word of the selected level
        '''
        count = len(self._wordList[level])
        fickleFingerOfFate = randint(0,count-1)
        return self._wordList[level][fickleFingerOfFate]
    
    def countWords(self, level):
        '''
        How many words do we have?
        '''
        return self._wordCount[level]
    
    def deleteWord(self, word):
        '''
        Delete a word from the list.
        '''
        # TODO:
        pass
    
    def levelDescription(self, level):
        '''
        Get the description for the word levels. If there are no words available of that level, no description is returned.
        '''
        if self._wordCount[level] > 0:
            return self._levelDescription[level]
        else:
            return ""
        
    def maxLevel(self):
        '''
        What is the max level that can be played?
        '''
        return self._maxLevel
    
