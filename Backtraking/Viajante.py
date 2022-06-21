# -*- coding: utf-8 -*-
"""
Created on Thu May 13 18:48:46 2021

@author: Juan Manuel Real
"""
import math


#Función principal que se encargará de realizar el BackTraking
def viaje(matriz,n,e,booleanos,orden,d,ordenaux,daux):
    #Creamos una variable iteradora con valor igual a 1, porque el valor 0 es fijo, dado que empezaremos el recorrido por este punto.
    i = 1
    #Mientras que no hayamos explorado todas las opciones, continuamos.
    while i<n:
        #Si no nos encontramose en la última iteración
        if(e<n-1):
        
            #Si la ciudad aún no ha sido explorada, la indicamos como explorada y sumamos la distancia que recorreriamos
            if(not booleanos[i]):
                #Hacemos exactamente lo mismo que en el anterior if, donde aún no teníamos una solución propuesta.
               booleanos[i]=True
               ordenaux[e]=i
               #Guardamos la distancia en una variable para reducir complejidad, ya que así nos ahorramos la búsqueda dos veces, aquí y más adelanta en la resta.
               dist=matriz[i][ordenaux[e-1]]
               daux[0]+=dist
               
               #Ahora comprobamos a modo de poda, si la distancia que llevamos recorrida, es menor que la que tenemos ya como distancia mínima. De esta manera
               #nos ahorramos búsquedas en caso de que el recorrido actual sea mayor que el mínimo actual. Si cumple el requisitos llamamos recursivamente.
               if(daux[0]<d[0] or d[0]<=0 ):
                   viaje(matriz,n,e+1,booleanos,orden,d,ordenaux,daux)
               
                #Restauramos los valores para poder seguir buscando una ruta más óptima.
               daux[0]-=dist
               booleanos[i]=False
               ordenaux[e]=-1
         
        #Si nos encontramos en la última ciudad
        else:
            #Si la ciudad está aún libre
            if(not booleanos[i]):
                #La indicamos como visitada y la colocamos en el orden que corresponda, que debería de ser el último.
                booleanos[i]=True
                ordenaux[e]=i
                dist=matriz[i][ordenaux[e-1]]+matriz[i][ordenaux[0]]
                #Sumamos las distancias, tanto con la ciudad anterior como con la primera visitada. Ya que la ruta es circular.
                daux[0]+=dist
                
                #Si la distancia que acabamos de hallar en este recorrido es menor que la que teníamos propuesta, entramos al bucle.
                #Además, en el caso de que se trate de la primera solución propuesta, entraremos si o si.
                if(daux[0]<d[0] or d[0]<=0):
                    
                    #Copiamos posición a posición el vector orden que hemos ido rellenando en esta rama en el que es la mejor solución.
                    for j in range(n):
                        orden[j]=ordenaux[j]
                    
                    #orden=ordenaux.copy() 
                    
                    #orden=ordenaux[:]
                    
                    #Guardamos la nueva distancia solución
                    d[0]=daux[0]
                    
                #Deshacemos los cálculos hechos en esta iteración, para poder seguir buscando una solución óptima.   
                daux[0]-=dist
                booleanos[i]=False
                ordenaux[e]=-1
        
        #daux[0]-=matriz[ordenaux[e]][ordenaux[e-1]]
        
        i+=1
    
#Creamos las variables que nos servirán para realizar el cálculo.   
n=int(input(""))
coordX=[0]*n
coordY=[0]*n
booleanos=[False]*n
orden=[-1]*n
ordenaux=[-1]*n
d=[0.0]
daux=[0.0]




for i in range(n):
    entrada=input("").split(" ")
    coordX[i]=float(entrada[0])
    coordY[i]=float(entrada[1])


#Para simplificar el cálculo y reducir complejidad al no tener que estar calculando las distancias cada vez que las necesitemos, vamos a crear
#una matriz que almacene las distancias entre todas las ciudades entre sí.
matriz = []

for i in range (n):
    matriz.append([])
    for j in range(n):
        if(i==j):
            matriz[i].append(0)
        else:
           matriz[i].append(math.sqrt(((coordX[i]-coordX[j])**2+(coordY[i]-coordY[j])**2)))

#Ponemos la ciudad inicial como visitada ya que es donde empezaremos, además la pondremos como la primera ciudad visitada.
booleanos[0]=True
orden[0]=0
ordenaux[0]=0

#Llamamos al BackTraking
viaje(matriz,n,1,booleanos,orden,d,ordenaux,daux)

#Como se especifica en el enunciado, la primera ciudad visitada (después de la de partida) debe de ser menor que el de la última
#Así que lo comprobamos y en caso de que la ruta calculada haya sido al revés, damos la vuelta al vector y ponemos la posición 0 
#en el inicio (ya que al darle la vuelta, esta se irá al final)
if(orden[n-1]<orden[1]):
    orden.pop(0)
    orden.reverse()
    orden.insert(0,0)

#Imprmimos el resultado como lo pide
print("%.4f"%d[0])

for i in range (n):
    if(i<n-1):
        print(orden[i],end=" ")
    else:
        print(orden[i],end="")