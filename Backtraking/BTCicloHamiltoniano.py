# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:38:11 2021

@author: Juan Manuel Real
"""
def cicloHamiltoniano(grafo,recorrido,e,libre,encontrado):
    j=0
    tam=len(grafo)-1
    if(e<=tam):
        while j<2:
            if(j==0):
                for i in range(tam+1):
                    if(not(encontrado[0])):
                        llevamos=len(recorrido)-1
                        libre[e]=False
                        recorrido.append(e)
                        llevamos+=1
                    
                    
                    if((llevamos)==(tam) and (grafo[recorrido[0]][recorrido[llevamos]]==1) and not(encontrado[0])):
                        recorrido.append(recorrido[0])
                        encontrado[0]=True
                        '''
                        print("SOLUCION ENCONTRADA")
                        print(recorrido)
                        '''
                        
                    
                    if(grafo[e][i]==1 and libre[i] and not(encontrado[0])):
                        
                        '''
                        print("Etapa: "+str(e))
                        print("Pasamos al punto: "+str(i))
                        print("camino: "+str(recorrido))
                        print("Libres: "+str(libre))
                        print("------")
                        input("")
                        '''
                        
                        cicloHamiltoniano(grafo,recorrido,i,libre,encontrado)
                    if(not(encontrado[0])):      
                        libre[e]=True
                        recorrido.pop(llevamos)
                        
            else:
                '''
                print("*******")
                print("no tomamos como candidata la etapa: "+str(e))
                print("Pasamos a la etapa: "+str(e+1))
                print("camino: "+str(recorrido))
                print("Libres: "+str(libre))
                print("*******")
                '''
            
            j+=1
            


matriz=[[0,1,0,0,0,0,1,0],
        [1,0,0,0,0,1,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,1,0,0,0,0,1],
        [0,1,0,1,0,0,1,0],
        [1,0,0,0,0,1,0,1],
        [0,0,0,0,1,0,1,0]]

'''
matriz=[[0,1,1,1,1,0,0],
        [1,0,0,0,0,1,1],
        [1,0,0,0,1,1,0],
        [1,0,0,0,0,1,1],
        [1,0,1,0,0,1,0],
        [0,1,1,1,1,0,1],
        [0,1,0,1,0,1,0]]
'''

libre=[True]*len(matriz)

recorrido= []

cicloHamiltoniano(matriz,recorrido,0,libre,[False])

print(recorrido)

