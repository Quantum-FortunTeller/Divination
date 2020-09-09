# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:30:38 2020

@author: Kyle
"""
zdic = {}
with open('64.txt', encoding = 'utf8') as zfile:
    for line in zfile:
        z = line.split(' ', 1)
        key = z[0]
        value = z[1].split('，',1)
        zdic[key] = value
        
        
for x,y in zdic.items():
    print('%s %s %s' %(x,y[0],y[1])) 

    

