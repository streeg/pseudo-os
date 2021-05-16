import sys
import processModule  as pm

class Reader():

    def readModule(self):
        chosenModule = sys.argv[1]  # receive a number {1,2,3} and assign a module.
        fileName = sys.argv[2]      # receive a file.txt {process, memory, inout} and read its content.

        if(chosenModule == "1" and fileName == "processes/processes.txt"):
            process = pm.Process()
            #Should create a method for this in processModule
            file = open(fileName, "r")
            fileLines = file.readlines()
            processInfo = [(x.strip()).split('\n') for x in fileLines]
            for line in processInfo:
                for stringNumber in line:
                    a_list = stringNumber.split()
                    map_object = map(int, a_list)
                    list_of_integers = list(map_object)
                    for x in list_of_integers:
                        process.receiveContent(x)
        
