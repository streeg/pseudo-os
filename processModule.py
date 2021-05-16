import sys
import firstInFirstOut as ff
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
        

    
    def shortestJobFirst(self, listOfNumbers):
        print("shortestJobFirst algorithm")    

    
    def roundRobin(self, listOfNumbers):
        print("roundRobin algorithm")    