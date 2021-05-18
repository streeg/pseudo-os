import sys
import numpy as np
import pandas as pd
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


    def lru(self,nr_frames,pages):
        count_faults = 0
        elem_maior_indice = 0
        maior_indice = 0
        pages_in_mem_2 = list()
        pages_used = list()
        for i in range(len(pages)):
     
            if np.isin(pages[i],pages_in_mem_2):
               pages_used.append(pages[i])
            else:
                if(len(pages_in_mem_2)<nr_frames[0].astype(int)): # verifica se ainda tem espaco no frame
                    pages_in_mem_2.append(pages[i])
                    pages_used.append(pages[i])
                    count_faults +=1
                else:               
                    temp_list = pages_used[::-1]
                    maior_indice = 0
                    for k in range(len(pages_in_mem_2)):
                        page_item = pages_in_mem_2[k]    
                        if (temp_list.index([page_item]) >= maior_indice): # descobre a pagina com maior indice
                            maior_indice = temp_list.index([page_item]) # salva esse indice
                            elem_maior_indice = temp_list[maior_indice] # salva a pagina com maior indice
                    

                    for j in range(len(pages_in_mem_2)):
                        if(pages_in_mem_2[j] == elem_maior_indice):
                            pages_in_mem_2[j] = pages[i]
                    count_faults +=1
                    pages_used.append(pages[i])

        print("LRU {}".format(count_faults))

    def sc(self, fileName): 
        
        def process_exists(process, pages):
            for page in pages:
                if page[0] == process:
                    return True
            return False

        def process_index(process, pages):
            for i, page in enumerate(pages):
                if page[0] == process:
                    return i

        def manage_rbit(pages):

            while pages[0][1] != 0:
                pages[0][2] += 1
                if pages[0][2] == 3:
                    pages[0][1] = 0
                pages.append(pages[0])
                del(pages[0])
            
            del(pages[0])

        fp = open(fileName, 'r')
        lines = fp.readlines()
        total_frames = int(lines[0])
        pages = []
        fault = 0

        # [no_pagina, r_bit, mem_ref]

        for line in lines[1:]:
            process = int(line)
            # for i, page in enumerate(pages):
            #     pages[i][2] += 1
            #     if pages[i][2] == 3:
            #         pages[i][1] = 0

            if len(pages) < total_frames:
                if process_exists(process, pages):
                    i = process_index(process, pages)
                    pages[i][1] = 1
                    pages[i][2] = 0
                else:
                    fault += 1
                    pages.append([process, 1, 0])
            
            else:
                if process_exists(process, pages):
                    i = process_index(process, pages)
                    pages[i][1] = 1
                    pages[i][2] = 0
                else:
                    fault += 1
                    manage_rbit(pages)
                    pages.append([process, 1, 0])
                    
        fp.close()

        print('SC ', fault)
