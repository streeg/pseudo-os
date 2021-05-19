import sys
import numpy as np
from memory import firstInFirstOut as ff
from memory import lastRecentlyUsed as lru
from memory import secondChance as sc

class Memory():


    def getPages(self, fileName):
        file = open(fileName, "r")
        fileLines = file.readlines()
        processInfo = np.asarray([(x.strip()).split('\n') for x in fileLines])
        listOfNumbers = []
        for line in processInfo:
            listOfNumbers.append(list(line.astype(int)))
        numberFrames  = listOfNumbers[0]
        listOfNumbers = listOfNumbers[1:]
        return numberFrames,listOfNumbers    

    def fifo(self, numberFrames, pages):
        firstInFirstOut = ff.firstInFirstOut()
        firstInFirstOut.processData(numberFrames, pages)


    def lru(self, numberFrames, pages):
        lastRecentlyUsed = lru.lastRecentlyUsed()
        lastRecentlyUsed.processData(numberFrames, pages)


    def sc(self, fileName): 
        secondChance = sc.secondChance()
        secondChance.processData(fileName)

