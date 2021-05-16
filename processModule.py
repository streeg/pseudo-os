import sys
class Process():
    
    def receiveContent(self, processNumber):
        print(processNumber)

    def manipulableContent(self, fileName):
        file = open(fileName, "r")
        fileLines = file.readlines()
        processInfo = [(x.strip()).split('\n') for x in fileLines]
        list_of_integers = []
        for line in processInfo:
            for stringNumber in line:
                a_list = stringNumber.split()
                map_object = map(int, a_list)
                list_of_integers += list(map_object)
        return list_of_integers

    def firstInFirstOut(self, fileName):
        print("firstInFirstOut algorithm")

    
    def shortestJobFirst(self, fileName):
        print("shortestJobFirst algorithm")    

    
    def roundRobin(self, fileName):
        print("roundRobin algorithm")    