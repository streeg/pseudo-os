#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 00:47:20 2021

@author: roberta
"""


class shortestSeekTimeFirst:
    
    def processData(self, fileName):
        moves = 0
        fp = open(fileName, 'r')
        lines = fp.readlines()
        # number_of_cylinders = int(lines[0])
        if len(lines) > 2:
            init_head = int(lines[1])
            req = lines[2:]
            req = [int(r) for r in req]
        
            number_of_req = len(req)
            while number_of_req > 0:
                
                distances = [abs(r - init_head) for r in req]
                min_distance = min(distances)
                i = distances.index(min_distance)
    
                # i, m = short_distance(req,init_head)
                moves += min_distance
                init_head = req[i]
                req = [r for r in req if r!=req[i]]
                number_of_req -= 1
            
        fp.close()
        print('SSF ', moves)
        