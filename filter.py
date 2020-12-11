# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:06:05 2019

@author: andok
"""
import numpy as np
import random as rd

print("### People generator")
session = input("Choose session name : " )
fem_firstfile = input("Choose female firstnames file : " )
ff = open(fem_firstfile)
male_firstfile = input("Choose male firstnames file : " )
mf = open(male_firstfile)
lastfile = input("Choose lastnames file : " )
l = open(lastfile)
number = int(input("How many people? "))



fem_names = ff.readlines()
male_names = mf.readlines()
fam_names = l.readlines()
ff.close()
mf.close()
l.close()

file_people = open("generated/"+session+"_people.csv","w")

for i in range(number) :
    age = str(max(int(rd.normalvariate(30, 10)),1))
    if rd.randint(0,1) == 1 :
        genre = "f"
        i = rd.randint(0,len(fem_names)-1)
        firstname = fem_names[i]
    else :
        genre = "m"
        i = rd.randint(0,len(male_names)-1)
        firstname = male_names[i]
        
    i = rd.randint(0,len(fam_names)-1)
    lastname = fam_names[i]
    s = firstname[:-1] +" ;"+ lastname[:-1] +";"+genre +";"+age+"\n"
    file_people.write(s)
file_people.close()
print("done")
    