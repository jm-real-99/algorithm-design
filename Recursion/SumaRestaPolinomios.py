# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:23:50 2021

@author: Juan Manuel Real

Se ha realizado un cambio respecto al anterior fichero mandado, que ya pasó el juez, debido a que para el apartado 3,
me he dado cuenta que las operaciones de suma y resta no me servían con el código implementado para multiplicar polinomios.
"""

import math

def impresionPolinomio(vector,x,grado,poli):
    if((grado==0) and ((vector[0])==0)):
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
        
def sumaPolinomio(p,q,n):
    #Si ya nos hemos pasado del tamaño de ambos vectores, entonces terminamos la recursividad y devolvemos una lista vacía
    if(len(p)<=n and len(q)<=n):
        return []
    #Si aún tenemos ambos vectores, los operamos con ellos y concatenamos el resultado con lo que nos venga de la llamada recursiva
    elif(len(p)>n and len(q)>n):
        return [p[n]+q[n]]+sumaPolinomio(p,q,n+1)
    
    #En el caso de que ambos polinomios no sean del mismo tamaño, operamos solo con el que aún nos queden posiciones por contar.
    elif(len(p)>n and len(q)<=n):
        return [p[n]]+sumaPolinomio(p,q,n+1)
    elif(len(p)<=n and len(q)>n):
        return [q[n]]+sumaPolinomio(p,q,n+1)

def restaPolinomio(p,q,n):
    #Misma explicación que la suma, pero realizando la operación resta.
    if(len(p)<=n and len(q)<=n):
        return []
    elif(len(p)>n and len(q)>n):
        return [p[n]-q[n]]+restaPolinomio(p,q,n+1)
    elif(len(p)>n and len(q)<=n):
        return [p[n]]+restaPolinomio(p,q,n+1)
    elif(len(p)<=n and len(q)>n):
        return [-q[n]]+restaPolinomio(p,q,n+1)
        
n1=int(input(""))
v1=(input("")).split(" ")
polinomio1=[]
for i in range (n1+1):
    polinomio1.append(int(v1[i]))
    
n2=int(input(""))
v2=(input("")).split(" ")
polinomio2=[]
for i in range (n2+1):
    polinomio2.append(int(v2[i]))

suma=sumaPolinomio(polinomio1,polinomio2,0)
resta=restaPolinomio(polinomio1,polinomio2,0)

impresionPolinomio(suma,len(suma)-1,len(suma)-1,"")
impresionPolinomio(resta,len(resta)-1,len(resta)-1,"")


    
    