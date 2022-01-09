#!/usr/bin/env python
from random import randint
import pyperclip
import sys
import ctypes
import clipboard

ctypes.windll.kernel32.SetConsoleTitleW("Bombparty Cheat")

'''CHANGE TO YOUR OWN PATH'''
path = "C:/Users/fyannz/Desktop/stuff/bombpartycheatt/web2"


''' BOMB PARTY BOT'''

    
wordlistone = open(path)

stringone = wordlistone.read()

while True:
    arrayOfWords = []
    print ('------------------------------')
    print ('')
    print ('type exit to close program')
    var = input("Please enter part of a word: ")
    print ('')

    if var == "exit":
        wordlistone.close()
        sys.exit(0)

    for line in stringone.splitlines():
        if var in line:
            arrayOfWords.append(line)
            
    matchingWord = arrayOfWords[randint(0,len(arrayOfWords))]
    pyperclip.copy(matchingWord)
    print (matchingWord)
    print ('')
    
        
        
wordlistone.close()

clipboard.copy(matchingWord)
