import sys
import numpy as np
#from inout import firstComeFirstServe as fcfs
#from inout import shortestSeekTimeFirst as sstf
from inout import elevator as scan

class Inout():

    #def fcfs(self, fileName):
    #    firstComeFirstServe = fcfs.firstComeFirstServe()
    #    firstComeFirstServe.processData()

    #def sstf(self, fileName):
    #    shortestSeekTimeFirst = sstf.shortestSeekTimeFirst()
    #    firstComeFirstServe.processData()
        
    def scan(self, fileName):
        elevator = scan.elevator()
        elevator.processData(fileName)
                