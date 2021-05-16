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
        #takes only the first element of each tuple
        n = 0
        arrivalTime = [x[n] for x in listOfNumbers]
        print(arrivalTime)
        #takes only the second element of each tuple
        n = 1
        serviceTime = [x[n] for x in listOfNumbers]
        print(serviceTime)
        

    
    def shortestJobFirst(self, listOfNumbers):
        print("shortestJobFirst algorithm")    

    
    def roundRobin(self, listOfNumbers):
        print("roundRobin algorithm")    