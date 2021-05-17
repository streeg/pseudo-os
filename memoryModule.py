import sys
import numpy as np
class Memory():

    def getPages(self, fileName):
        file = open(fileName, "r")
        fileLines = file.readlines()
        processInfo = np.asarray([(x.strip()).split('\n') for x in fileLines])
        listOfNumbers = []
        for line in processInfo:
            listOfNumbers.append(list(line.astype(int)))
        nr_frames  = listOfNumbers[0]
        listOfNumbers = listOfNumbers[1:]
        return nr_frames,listOfNumbers    

    def fifo(self,nr_frames,pages):
        count_faults = 0
        control_frame_exit = 0
        pages_in_mem = list()
        for i in range(len(pages)):
            if np.isin(pages[i],pages_in_mem):
               pass
            else:
                if(len(pages_in_mem)<nr_frames[0].astype(int)):
                    pages_in_mem.append(pages[i])
                    count_faults +=1
                else:
                    pages_in_mem[control_frame_exit] = pages[i]
                    control_frame_exit += 1
                    if(control_frame_exit == nr_frames[0].astype(int)):
                        control_frame_exit = 0
                    count_faults +=1
        print("FIFO {}".format(count_faults))
                    