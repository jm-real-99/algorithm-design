# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:42:38 2021

@author: Juan Manuel Real
"""

##Funcion auxiliar hecha en un problema en clase
def busquedaBinaria(vector, tmin,tmax,n):
    aux=int((tmax-tmin)/2) #Calculamos el valor medio de nuestro vector
    pos=tmin+aux #Calculamos nuestra posicion relativa
    if(tmin==tmax): #Si hemos reducido a una posicion nuestro vector, solo hay dos opciones
        #if(vector[tmin]==n): #Valor del vector igual a nuestro n
        return tmin
    elif(pos==tmin): ##En este caso tendremos dos posiciones posibles 
        if(n > vector[pos]):
            return pos+1
        else:
            return pos
    else: #En este caso, no hemos acabado el problema,así que seguiremos reduciendo recursivamente.
        if(n==vector[pos]): #Si hemos encontrado nuestro elemento, paramos y devolvemos el resultado 
            return pos
        elif (n>vector[pos]): #Si nuestro n es mayor que el elemento medio de la lista, entonces llamamos recursivamente
        #llamando a la mitad superior del vector.
            return busquedaBinaria(vector, pos,tmax,n)
        else: #Si no, llamamos a la mitad infrerior
            return busquedaBinaria(vector, tmin,pos,n)
        
def insertarListaOrdenada (vector,numero):
    tam = len (vector) -1
    if(tam == -1): #Si es -1 es que la longitud del vector es 0. Terminamos insertando directamente el numero
        vector.append(numero)
    elif(n<=vector[0]): #Si el numero es menor que el primer elemento de la lista, directamente lo introducimos en la primera posicion
        vector.insert(0,numero)
    elif(n>=vector[tam]): #Si el numero es mayor que el ultimo elemento de la lista, directamente lo introducimos en la ultima posicion
        vector.insert(tam+1,numero)
    else: #Si no tenemos tanta suerte en los anteriores casos,entonces operamos normalmente.
        posicion = busquedaBinaria(vector, 0, tam, numero)
        vector.insert(posicion,numero)
        
        
tam=int(input(""))
v=(input("")).split(" ")
vector = []
for i in range (tam):
    vector.append(int(v[i]))

n=int(input(""))

insertarListaOrdenada(vector,n)

for i in range (tam+1):
    if(i==tam):
        print(str(vector[i]),end='')
    else:
        print(str(vector[i])+" ",end='')
