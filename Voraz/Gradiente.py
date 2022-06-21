# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:44:40 2021

@author: Juan Manuel Real
"""
#Esta función auxiliar nos calculará la matriz transpuesta de matrizO y se guardará en matrizT
def transpuesta(matrizO,matrizT):

    n=len(matrizO)
    m=len(matrizO[0])
    for j in range(m):
        aux=[]
        for i in range (n):
            aux.append(matrizO[i][j])
        matrizT.append(aux)


#Esta función auxiliar nos calculará la multiplicación de la matriz1 y el vector v2, y se guardará en resultado
def multMatrizVector(matriz1,v2,resultado):
    n1=len(matriz1)
    m1=len(matriz1[0])

    for i in range(n1):
        acumulador=0
        for j in range(m1):
            acumulador+= matriz1[i][j] * v2[j]
        
        resultado.append(acumulador)

#Esta funcion auxiliar nos calculará la multiplicación de la matriz matriz y el escalar escalar y se guardará en resultado.
def multMatrizEscalar(matriz,escalar,resultado):
    n=len(matriz)
    m=len(matriz[0])
    
    for i in range(n):
        aux=[]
        for j in range(m):
            aux.append(matriz[i][j]*escalar)
        resultado.append(aux)
    

#Esta función auxiliar nos calculará la resta de los vectores vector1y vector2 y se guardará en resultado
def restaVectores(vector1,vector2,resultado):
    n=len(vector1)
    
    for i in range(n):
            resultado.append(vector1[i]-vector2[i])


#Esta función auxiliar calcularemos el módulo del vector dado y lo devolveremos en una variable.
def modulo(vector):
    acum=0
    for i in range(len(vector)):
        acum+=vector[i]**2
        
    acum=acum**0.5

    return acum

#En esta función calcularemos el gradiente, basandonos en el pseudocódigo dado en el enunciado de la práctica.
def gradiente(n,m,matrizA,vectorb,realesXo,alpha,error):
    #Copiamos en la variable x el vector realesXo, que será el vector que guarde las x
    x=realesXo[:]
    #Creamos la matriz transpuesta y la calculamos.
    trans=[]
    transpuesta(matrizA,trans)
    #Creamos la matriz resultado de la operacion 2*At.
    porEscalar2=[]
    multMatrizEscalar(trans,2,porEscalar2)
    #Creamos la matriz resultado de la operacion (2*At)*b
    mporb=[]
    multMatrizVector(porEscalar2,vectorb,mporb)
    
    #Las variables calculadas anteriormente, se hacen fuera del bucle while, debido a que estás serán las mismas durante 
    #todas las iteraciones. Así de este modo, nos ahorramos complejidad al reducir los cálculos de los mismos datos repetidas veces.
    
    #Simulamos ciclo do-while
    while(True):
        #Creamos las siguientes variables
        mporX=[] #Resultado de multiplicar A*x
        MatxVector=[] #Resultado de multiplicar (2*At)*(A*x)
        resta=[] #Resultado de la resta que daría la solución del gradiente, siendo esta la fórmula dada: ((2*At)*(A*x)) - ((2*At)*b)
        
        #Hacemos los cálculos anteriormente dichos
        multMatrizVector(matrizA,x,mporX)
        multMatrizVector(porEscalar2,mporX,MatxVector)
        restaVectores(MatxVector,mporb,resta)
        
        #Calculamos el módulo del resultado de la resta.
        gradiente=modulo(resta)
        
        #Comprobamos que el módulo del gradiente sea menor que el error dado. Si lo es, entonces hacemos un break que romprerá la ejecución del 
        #bucle while. Así habríamos terminado.
        if(gradiente<=error):
            break
        #Si no hemos hecho el break, entonces continuamos.
        else:
            #Hacemos la actualizacion del gradiente, multiplicandolo por alpha
            for i in range(len(resta)):
                resta[i]=resta[i]*alpha
            
            #Actualizamos la x.
            for i in range(len(x)):
                x[i] =x[i]-resta[i]
                
    #Si hemos terminado, entonces imprimimos según se nos especifica.
    for i in range(len(x)):
        if(i==(len(x)-1)):
            print("%.4f" %x[i], end="")
        else:
            print("%.4f" %x[i], end=" ")
                
            
        
x = input("").split(" ")
n=int(x[0])
m=int(x[1])


matrizA = []
for i in range(n):
    x=(input("").split(" "))
    aux=[]
    for j in range(m):
        aux.append(int(x[j]))
    matrizA.append(aux)
        
    
vectorb = []
x=input("").split(" ")
for i in range(n):
    vectorb.append(int(x[i]))


realesXo=[]
x=input("").split(" ")
for i in range(m):
    realesXo.append(float(x[i]))


alpha = (float(input("")))

error= (float(input("")))

gradiente(n,m,matrizA,vectorb,realesXo,alpha,error)

#0.0000000001