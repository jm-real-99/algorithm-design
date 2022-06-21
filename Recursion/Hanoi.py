# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:34:28 2021

@author: Juan Manuel Real
"""

def hanoi(disco, origen,destino,otro):
    if(disco==1):
        ##Si estamos con el disco más pequeño, lo movemos directamente de un extremo a otro. 
        print("Mueve disco "+str(disco)+" desde torre "+str(origen)+" a torre "+str(destino))
        print("Mueve disco "+str(disco)+" desde torre "+str(destino)+" a torre "+str(otro))
    else:
        ##Llamamos recursivamente al problema, moviendo los discos hacia el palo 3
        hanoi(disco-1,origen,destino,otro)
        print("Mueve disco "+str(disco)+" desde torre "+str(origen)+" a torre "+str(destino))
        ##Llamamos recursivamente al problema, moviendo los discos menores hacia el palo 1
        hanoi(disco-1,otro,destino,origen)
        print("Mueve disco "+str(disco)+" desde torre "+str(destino)+" a torre "+str(otro))
        ##Finalmente, si hemos llegado aquí, colocamos los discos menores que el nuestro encima nuestra en el palo 3.
        hanoi(disco-1,origen,destino,otro)
        
    
n=int(input(""))
hanoi(n,1,2,3) 