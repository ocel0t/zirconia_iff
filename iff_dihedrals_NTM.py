# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:58:09 2022

@author: Tamás Milán Nagy

@INFO
The following script generates missing dihedral term entries.

Input (file): user defined filename+extension with the missing dihedral terms 
Example input file (from Materials Studio error output):
'''
Error: Energy expression: cannot find parameters for torsion: O8(ozr1)-Zr4(zr2)-O3(ozr7)-Zr3(zr4)
Error: Energy expression: cannot find parameters for torsion: O3(ozr7)-Zr4(zr2)-O8(ozr1)-Zr1(zr1)
Error: Energy expression: cannot find parameters for torsion: O3(ozr7)-Zr4(zr2)-O8(ozr1)-Zr3(zr4)
'''

Input (data): user defined version, reference, but dihedral parameters are all set to 0.
Output: bonded terms on the screen.

Usage: execute iff_dihedrals_NTM.py and follow screen instructions.

"""

import os
from glob import glob
import re


name = str(input("Please enter input file name to process: "))
Ver = str(input("Please enter version (Ver): "))
Ref = str(input("Please enter the reference (Ref): "))

currDir = os.getcwd()
files_list = glob(os.path.join(currDir , name))

file1 = open(name, 'r')
Lines = file1.readlines()
file1.close()

result=""
atypes=[]
count=0
final=""  

for i in Lines:
    atypes += re.findall(r'\(.*?\)', i)

for e in atypes:
    if count<4:
        e1=e.replace("(","")
        e2=e1.replace(")","")
        result+=str(e2+"   ")
        #print(result)
        count+=1
    else:
        count=1
        final+=str(" "+Ver+"  "+Ref+"     "+result+ "0.00000      " +"3      "+"0.00000      "+"\n")
        e1=e.replace("(","")
        e2=e1.replace(")","")
        result=str(e2+"   ")
        #print(result)
        print(final)
    
    
    
    

