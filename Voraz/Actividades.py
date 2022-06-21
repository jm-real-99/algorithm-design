# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:26:04 2021

@author: Juan Manuel Real
"""

#tomando como referencia el pseudocódigo iterativo dado en el apartado 16.1 del libro "Introduction to Algorithms"
def actividades(n,tareas):
    cont=1  #Variable contador que nos ayudará a ir contando el numero de actividades del subconjunto, iniciamos en 1, porque ya contamos con la primera actividad.
    k=0     #Variable con la que iremos mirando el final de las actividades
    for m in range(1,n):
        #Si la posicion de comienzo de la tarea m es mayor que el final de la tarea k, entonces la tomamos como siguiente tarea que se va a realizar
        if(tarea[m][1]>=(tarea[k][0])):
            cont+=1;
            k=m
    
    print(cont)
    
    
    
n=int(input(""))
v1=(input("")).split(" ")
v2=(input("")).split(" ")

#Tarea será una lista de enteros compuestos tal que [(f1,s1),(f2,s2),...,(fn,sn)]
#donde fx será indicará el final de la tarea x y sx será el principio de la tarea x
tarea=[] 
for i in range (n):
    tarea.append((int(v2[i]),int(v1[i])))
    
#Ordenamos la lista tarea de tal manera que las que terminen antes vayan al principio. De esta manera, 
#nos facilita el cálculo de las actividades que se van a realizar, ya que así, en el paso de comparar 
#si la posicion de comienzo de una tarea es mayor que el final de la actividad a realizar, podremos hacerlo de una 
#manera más escalada y ordenada.
tarea.sort()

#print(tarea)
    
actividades(n,tarea)



##ordenamos(n,comienzo,final,[],[])


#11
#1 2 0 5 8 5 6 8 3 3 12
#4 13 6 7 12 9 10 11 8 5 14

#9
#7 0 11 4 3 9 6 0 9
#9 7 14 10 7 12 10 3 10