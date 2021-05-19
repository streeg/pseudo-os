# -*- coding: utf-8 -*-
import sys
import numpy as np

from processes import processModule as pm
from memory import memoryModule as mm
from inout import inoutModule  as iom


class Reader():

    def readModule(self):

        chosenModule = sys.argv[1]  # receive a number {1,2,3} and assign a module.
        fileName = sys.argv[2]      # receive a file.txt {process, memory, inout} and read its content.
        try:
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

            if(chosenModule == "2" and fileName == "memory/test/memory.txt"):
                print("Loading memory module...")            
                memory = mm.Memory()
                print("Memory loaded successfully!")
                print("Getting numbers from filename...")
                numberFrames,numberList = memory.getPages(fileName) # get number of frames availables and pages to be referenced
                print("Done!")
                print()
                print("--------------------------------------------------------------------------")
                print()
                getchar =  (input("Press enter to parse using First In First Out Algorithm"))
                memory.fifo(numberFrames,numberList)
                print()
                print("--------------------------------------------------------------------------")
                print()
                getchar =  (input("Press enter to parse using Second Chance Algorithm"))
                memory.sc(fileName)
                print()
                print("--------------------------------------------------------------------------")
                print()
                getchar =  (input("Press enter to parse using Last Recently Used Algorithm"))
                memory.lru(numberFrames,numberList)
                print()
                print("--------------------------------------------------------------------------")
                print()
                print("Done!")
                print("See you next time!")


            if(chosenModule == "3" and fileName == "inout/test/inout.txt"):
                print("Loading In Out module...")   
                inout = iom.Inout()
                print("In Out loaded successfully!")
                print("Getting numbers from filename...")
                print("Done!")
                print()
                print("--------------------------------------------------------------------------")
                print()
                getchar =  (input("Press enter to parse using First Come First Serve"))
                print()
                print("--------------------------------------------------------------------------")
                print()
                getchar =  (input("Press enter to parse using Shortest Seek Time First"))
                print()
                print("--------------------------------------------------------------------------")
                print()
                getchar =  (input("Press enter to parse using Elevator Algorithm (SCAN)"))
                inout(fileName)
                print()
                print("--------------------------------------------------------------------------")
                print()
                print("Done!")
                print("See you next time!")
            else:
                print("Error! Try again.")
                print("Remember the syntax should be:\n<python3 kernel.py $module $path>\n")
                print("Availabe modules:")
                print("1: Process\n2: Memory\n3: InOut\n")
                print("Availabe paths:")
                print("processes/test/testfile.txt\nmemory/test/testfile.txt\ninout/test/testfile.txt\n")
                getchar =  (input("Press enter to exit"))
                return 0
        
        except ValueError:
            print("Error trying to parse algorithms in the selected module")