# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:50:08 2021

@author: Juan Manuel Real
"""
#FUNCION AXUILIAR. Insertamos elemento de manera ordenada. Esto nos servirá para ir añadiendo al vector ordenado auxiliar.
def insertarElemento(v,n,pos):
    if(pos == 0):
        if(n<v[pos]):
            v.insert(0,n)
        else:
            v.insert(1,n)
            
    elif(n>=v[pos]):
        v.insert(pos+1,n)
    else:
        insertarElemento(v,n,pos-1)
    

def insertsort (vector, ordenado):
        if (len(vector) == 0): #Si hemos vaciado la lista original, es que la lista "ordenado" ya está ordenada y rellenada completamente
           #asi que imprimimos el vector ordenado
            for i in range (tam):
                if(i==tam-1):
                    print(str(ordenado[i]),end='')
                else:
                        print(str(ordenado[i])+" ",end='')
        elif (len(ordenado) ==0): #Esto ocurrirá en nuestra primera iteracion, por lo que metemos directamente la primera posicion del vector a
                        #la lista que vamos a ordenar.
            ordenado.append(vector.pop(0)) #Con pop extraemos el primer elemento, como si fuera una cola. 
            insertsort(vector,ordenado) #Llamamos recursivamente
        else:
            insertarElemento(ordenado,vector.pop(0), len(ordenado)-1) #insertamos el elemento de la lista original en la posicion correspondiente en el 
            #la lista ordenada. 
            insertsort(vector,ordenado) #Llamamos recursivamente
            
            
tam = int (input(""))
v=(input("")).split(" ")
vector = []
for i in range (tam):
    vector.append(int(v[i]))

insertsort(vector,[])


