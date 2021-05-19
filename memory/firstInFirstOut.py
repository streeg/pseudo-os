# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

class firstInFirstOut:

    def processData(self, numberFrames, pages):
        countPages = 0
        controlFrameExit = 0
        pagesInMem = list()
        for i in range(len(pages)):
            if np.isin(pages[i],pagesInMem):
               pass
            else:
                if(len(pagesInMem)<numberFrames[0].astype(int)):
                    pagesInMem.append(pages[i])
                    countPages +=1
                else:
                    pagesInMem[controlFrameExit] = pages[i]
                    controlFrameExit += 1
                    if(controlFrameExit == numberFrames[0].astype(int)):
                        controlFrameExit = 0
                    countPages +=1
        print("FIFO {}".format(countPages))