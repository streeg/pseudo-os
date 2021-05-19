# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

class lastRecentlyUsed:

    def processData(self, numberFrames, pages):
        countFaults = 0
        highestElementIndex = 0
        highestIndex = 0
        pagesInMemTwo = list()
        pagesUsed = list()
        for i in range(len(pages)):
     
            if np.isin(pages[i],pagesInMemTwo):
               pagesUsed.append(pages[i])
            else:
                if(len(pagesInMemTwo)<numberFrames[0].astype(int)): # verify empty space in frame
                    pagesInMemTwo.append(pages[i])
                    pagesUsed.append(pages[i])
                    countFaults +=1
                else:               
                    temp_list = pagesUsed[::-1]
                    highestIndex = 0
                    for k in range(len(pagesInMemTwo)):
                        page_item = pagesInMemTwo[k]    
                        if (temp_list.index([page_item]) >= highestIndex): # discover page with highest index
                            highestIndex = temp_list.index([page_item]) # save index
                            highestElementIndex = temp_list[highestIndex] # save page with highest index
                    

                    for j in range(len(pagesInMemTwo)):
                        if(pagesInMemTwo[j] == highestElementIndex):
                            pagesInMemTwo[j] = pages[i]
                    countFaults +=1
                    pagesUsed.append(pages[i])

        print("LRU {}".format(countFaults))