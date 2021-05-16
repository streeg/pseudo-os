# -*- coding: utf-8 -*-

import sys
import firstInFirstOut as ff
import shortestJobFirst as sjf
class Process():
    
    def receiveContent(self, processNumber):
        print(processNumber)

    def manipulableContent(self, fileName):
        file = open(fileName, "r")
        fileLines = file.readlines()
        processInfo = [(x.strip()).split('\n') for x in fileLines]
        listOfNumbers = []
        for line in processInfo:
            for stringNumber in line:
                mapObject = map(int, stringNumber.split())
                listOfNumbers.append(list(mapObject))
        return listOfNumbers    

    def fifo(self, listOfNumbers):
        firstInFirstOut = ff.firstInFirstOut()
        firstInFirstOut.processData(listOfNumbers)
        

    
    def sjf(self, listOfNumbers):
        shortestJobFirst = sjf.shortestJobFist()
        shortestJobFirst.processData(listOfNumbers)

    
    def roundRobin(self, listOfNumbers):
        print("roundRobin algorithm")    