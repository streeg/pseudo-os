# -*- coding: utf-8 -*-
import sys
import processModule  as pm

class Reader():

    def readModule(self):
        chosenModule = sys.argv[1]  # receive a number {1,2,3} and assign a module.
        fileName = sys.argv[2]      # receive a file.txt {process, memory, inout} and read its content.

        if(chosenModule == "1" and fileName == "processes/processes.txt"):
            process = pm.Process()
            numberList = process.manipulableContent(fileName)
            process.fifo(numberList)
            process.sjf(numberList)
            process.rr(numberList)