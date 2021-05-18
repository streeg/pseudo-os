# -*- coding: utf-8 -*-
import sys
from processes import processModule as pm
import inoutModule  as iom
import memoryModule as mm

class Reader():

    def readModule(self):

        chosenModule = sys.argv[1]  # receive a number {1,2,3} and assign a module.
        fileName = sys.argv[2]      # receive a file.txt {process, memory, inout} and read its content.
        if(chosenModule == "1" and fileName == "processes/test/processes.txt"):
            print("Loading process module...")
            process = pm.Process()
            print("Process loaded successfully!")
            print("Getting numbers from filename...")
            numberList = process.manipulableContent(fileName)
            print("Done!")
            print()
            print("--------------------------------------------------------------------------")
            print()
            getchar =  (input("Press enter to parse using First In First Out Algorithm"))
            process.fifo(numberList)
            print()
            print("--------------------------------------------------------------------------")
            print()
            getchar =  (input("Press enter to parse using Shortest Job First"))
            process.sjf(numberList)
            print()
            print("--------------------------------------------------------------------------")
            print()
            getchar =  (input("Press enter to parse using Round Robin. Please define the quantum manually."))
            process.rr(numberList)
            print()
            print("--------------------------------------------------------------------------")
            print()
            print("Done!")
            print("See you next time!")

        if(chosenModule == "3" and fileName == "in-out/inout.txt"):
            inout = iom.Inout()
            inout.scan(fileName)
