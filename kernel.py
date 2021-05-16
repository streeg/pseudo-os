# -*- coding: utf-8 -*-
#  This file is responsible for making calls to the other modules. 
 
import sys
import inoutModule  as iom
import processModule  as pm
import memoryModule as mm
import fileReader as fr

# Initialize the reader

reader = fr.Reader()
reader.readModule()







inout = iom.Inout()
inout.printInout()