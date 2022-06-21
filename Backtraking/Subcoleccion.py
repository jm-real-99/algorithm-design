# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:50:44 2021

@author: Juan Manuel Real
"""

#CASOS DE PRUEBA
#2 2 5 4 7
#6 14 8 1 6 7 14 7 5 4

#Funcion axiliar que nos servirá para contar los booleanos que llevamos en nuestro array
def cuenta(booleanos):
    n=0
    for i in (booleanos):
        if(i):
            n+=1
    return n

#Funcion axuiliar que nos servirá para saber cual es el número menor de nuestra sublista.
def menor(booleanos,C,n):
    for i in range(n):
        if(booleanos[i]):
            return C[i]

#Funcion auxiliar que nos servirá para ahorrarnos tiempo de ejecuciçon. Ya que si el tamaño del subconjunto
#m es 1. Entonces el número de solucines será igual al tamaño del vector original n.
def preSubcolecciones(n,C,m):
    if(m==1):
        print(n)
    else:
        #Si no se da el caso, entonces ordenamos el vector, para facilitarnos la ejecucion ya que enconces, según avanzamos en etapas, nos 
        #aseguramos que todos los números que vamos a evaluar son mayores que el número que vamos a optar como candidato a ser divisor.
        C.sort()
        #Creamos una lista de booleanos para ir marcando las opciones escogidas.
        booleanos = [False] * n
        #Creamos una variable solucion en la que iremos contando el nº de soluciones. Se crea como un array para 
        #pasarlo por referencia y que esta variable se cambie ACTUALIZE dentro de la funcion
        solucion=[0]
        subcolecciones(n,C,m,0,booleanos,solucion)
        print(solucion[0])
    
    
def subcolecciones(n,C,m,e,booleanos,solucion):
    
    i=0 #Creamos la variab le que nos servirá para iterar entre si ponemos la opcion como true o false.
    
    while i<=1:
        
        if(i==0):
            #Si es i es 0, significa que vamos a considerarla poner la posicion e en true.
            nsol=cuenta(booleanos) #Contamos los trues que llevamos mediante la funcion auxiliar.
            #Esto nos servirá para saber si hemos encontrado una solucion o no, 
            if(nsol==0):
                #Si todavía no hemos puesto ninguna solucion, marcamos si o si nuestra posicion como True.
                booleanos[e]=True
            elif(nsol<m):
                #Si ya tenemos alguna solución como candidata, evaluamos si nuestra posicion es dividible por el menor número del subconjunto.
                if(C[e]%menor(booleanos,C,n)==0):
                    #Si si que lo es, lo marcamos como candidato y sumamos una unidad a nuestra variable nsol
                    booleanos[e]=True
                    nsol+=1
                    #Si nsol es igual a m, es que hemos encontrado una solucion, así que la contamos.
                    if(nsol==m):
                        solucion[0]+=1
            #Si aún no hemos llegado al final del array C, si todavía no hemos encontrado una solucion y hemos contado con esta solucion,
            #entonces avanzamos en la búsqueda contando esta posicion como candidata.
            if(e<n-1 and nsol!=m and booleanos[e]):
                subcolecciones(n,C,m,e+1,booleanos,solucion)
        else:
            #Si estamos en i=1, significa que esta posición no es candidata. Así que contamos las posiciones candidatas que tenemos por el momento
            # y nos aseguramos de que nuestra posicion esté en false.
            booleanos[e]=False
            nsol=cuenta(booleanos)
            #Si aún nos quedan posiciones candidatas, nuestros candidatos son distintos al tamaño del subconjunto y aún nos quedan posiciones por
            #buscar, entonces continuamos con nuestra búsqueda.
            if(m<nsol+(n-e) and nsol!=m and e<n-1):
                 subcolecciones(n,C,m,e+1,booleanos,solucion)
        
        i+=1 #Sumamos una iteracion
                

n = int(input(""))
v=(input("")).split(" ")
vector = []
for i in range (n):
    vector.append(int(v[i]))
m=int(input(""))

preSubcolecciones(n,vector,m)
