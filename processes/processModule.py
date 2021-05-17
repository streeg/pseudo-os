# -*- coding: utf-8 -*-

import sys
from processes import firstInFirstOut as ff
from processes import shortestJobFirst as sjf
from processes import roundRobin as rr
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

    
    def rr(self, listOfNumbers):
        roundRobin = rr.RoundRobin()
        roundRobin.processData(listOfNumbers)