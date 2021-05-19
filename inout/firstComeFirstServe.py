#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 23:56:07 2021

@author: roberta
"""

class firstComeFirstServe:
    def processData(self, fileName):
        moves = 0
        fp = open(fileName, 'r')
        lines = fp.readlines()
        if len(lines) > 2:
            # number_of_cylinders = int(lines[0])
            init_head = int(lines[1])
            req = lines[2:]
            req = [int(r) for r in req]
        
        
            req.insert(0, init_head)
    

            for i,r in enumerate(req):
                if i < (len(req)-1):
                    moves += abs(req[i+1] - req[i])
        
        fp.close()
        print('FCFS ', moves)
        
        
        


        

#number_of_cylinder = 199 # numero de cilindros
#init_head = 53 # posição inicial da cabeça de leitura e gravação
#req = [98,183,37,122,14,124,65,67] # requisições

# FCFS > fila

#all_positions = req.insert(0, init_head)

#moves = 0
#for i,r in enumerate(all_positions):
#    if i < (len(all_positions)-1):
#        moves += abs(all_positions[i+1] - all_positions[i])
        
#print("FCFS =", moves) # a quantidade total de cilindros percorridos pela cabeça de leitura para atender todas as requisições de acesso ao disco


#moves = 0

# shortest seek time first

#print("SSF =", moves)