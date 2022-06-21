# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:14:55 2021

@author: Juan Manuel Real
"""
import math #Esta librería nos simplificará el calculo del valor absoluto

def impresionPolinomio(vector,x,grado,poli):
    if((grado==0) and 0((vector[0])==0)):
        print(" + 0") #Imprimimos el valor predeterminado. Caso excepcional 
    else:
        t=vector.pop(x)
        if(x==0):
            if(t>0):
                poli+=" + "+str(t)
            elif(t<0):
                t=int(math.fabs(t))
                poli+=" - "+str(t)
            print(poli)
        else:
            if(t>0):
                poli+=" + "+str(t)+"x^"+str(x)
            elif(t<0):
                t=int(math.fabs(t))
                poli+=" - "+str(t)+"x^"+str(x)
        
            impresionPolinomio(vector,x-1,grado,poli) ##Llamada a función recursiva. 

n=int(input(""))
v=(input("")).split(" ")

polinomio=[]
for i in range (n+1):
    polinomio.append(int(v[i]))
    

impresionPolinomio(polinomio,n,n,"")