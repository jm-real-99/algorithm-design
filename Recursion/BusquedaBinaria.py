# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:50:04 2021

@author: Usuario
"""

def busquedaBinaria(vector, tmin,tmax,n):
    aux=int((tmax-tmin)/2)
    pos=tmin+aux
    if(tmin==tmax):
        if(vector[tmin]==n):
            return tmin
        else:
            return -1
    elif(pos==tmin):
        if(n > vector[pos]):
            return pos+1
        else:
            return pos
    else:
        if(n==vector[pos]):
            return pos
        elif (n>vector[pos]):
            return busquedaBinaria(vector, pos,tmax,n)
        else:
            return busquedaBinaria(vector, tmin,pos,n)
        
vectorsito=[1,2,3,4,5,7,8,9,10]
print(len(vectorsito))
num = int (input("Introduce un num") )
pos=busquedaBinaria(vectorsito,0,len(vectorsito)-1,num)
print(pos)

        
        