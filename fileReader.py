import sys

class Reader():

    def readModule(self):
        chosenModule = sys.argv[1]  # receive a number {1,2,3} and assign a module.
        fileName = sys.argv[2]      # receive a file.txt {process, memory, inout} and read its content.
        file = open(fileName, "r")
        fileLines = file.readlines()
