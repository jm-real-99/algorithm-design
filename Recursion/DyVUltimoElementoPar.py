# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:03:58 2021

@author: Juan Manuel Real
"""

def ultimo_elemento_par(vector,i,f):
    if(f-i==1):
        if(vector[f]%2==0):
            return vector[f]
        elif((vector[i]%2==0)):
            return vector[i]
        else:
            return None
    else:
        mitad=int((f-i)/2)+i
        if(vector[mitad]%2==0):
            return ultimo_elemento_par(vector,mitad,f)
        else:
            return ultimo_elemento_par(vector,i,mitad)
        
#MAIN
v=[2,-4,10,8,0,12,9,3,-15,3,1]
#v=[2,4,6,7,5,3,7]
#v=[2,4,6,8,2,4]
#v=[3,3,3,3,3,3,3,3,3]
print(ultimo_elemento_par(v,0,(len(v)-1)))