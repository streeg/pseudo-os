# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

class secondChance:

    def processData(self, fileName):
        
        def processExists(process, pages):
            for page in pages:
                if page[0] == process:
                    return True
            return False

        def processIndex(process, pages):
            for i, page in enumerate(pages):
                if page[0] == process:
                    return i

        def manageRBit(pages):

            while pages[0][1] != 0:
                pages[0][1] = 0
                pages.append(pages[0])
                del(pages[0])
            
            del(pages[0])

        fp = open(fileName, 'r')
        lines = fp.readlines()
        total_frames = int(lines[0])
        pages = []
        fault = 0
        three = 0
        for line in lines[1:]:
            process = int(line)
            three += 1
            if three == 3:
                for page in pages:
                    page[1] = 0
                three = 0
                
            if len(pages) < total_frames:
                if processExists(process, pages):
                    i = processIndex(process, pages)
                    pages[i][1] = 1
                    
                else:
                    fault += 1
                    pages.append([process, 1])
            
            else:
                if processExists(process, pages):
                    i = processIndex(process, pages)
                    pages[i][1] = 1
                    
                else:
                    fault += 1
                    manageRBit(pages)
                    pages.append([process, 1])  
        fp.close()
        print('SC ', fault)
