# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:57:30 2021

@author: Juan Manuel Real
"""

import math

def impresionPolinomio(vector,x,grado,poli):
    if((grado==0) and ((vector[0])==0)):
        print(" + 0") #Imprimimos el valor predeterminado. Caso excepcional 
    elif((grado==-1) and ((vector)==[])):
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

def multiplicacion(p,q):

    
    n=min(len(p),len(q))
        
    if((max(len(p),len(q)))<=1): #Caso base, ya que entonces tenemos un numero unicamente.
        if(len(p)==0 or len(q)==0):
            return []
        else:
            resultado = []
            resultado.append(p[0]*q[0])
            return resultado
    else:
        #Dividimos las listas, con lista[:m] otendremos las posiciones desde 0 hasta m y con lista[m:] obtendremos las posiciones desde m hasta el final.
        mitad=int(n/2)
        
        if(mitad==0):
            mitad=1
        
        pb=p[:mitad] #pb corresponde a la mitad inferior del polinomio P
        pa=p[mitad:] #pa corresponde a la mitad superio del polinomio P
        qb=q[:mitad] #qb corresponde a la mitad inferior del polinomio Q
        qa=q[mitad:] #qa corresponde a la mitad superio del polinomio Q

        grado2m=[]
        gradom=[]
        
        for i in range (mitad*2):
            grado2m.append(0)
        
        for i in range (mitad):
            gradom.append(0)
        
        partemayor= multiplicacion(pa,qa)
        partemenor= multiplicacion(pb,qb)
        
        suma1=sumaPolinomio(pa,pb,0)
        suma2=sumaPolinomio(qa,qb,0)
        
        partemediana=multiplicacion(suma1,suma2)

        aux=restaPolinomio(partemediana,partemayor,0)

        medio=restaPolinomio(aux,partemenor,0)

        ##Concatenamos
        partemayor=grado2m+partemayor
        medio=gradom+medio
        
        sumaMayorMediano=sumaPolinomio(partemayor, medio,0)
        resultado=sumaPolinomio(sumaMayorMediano, partemenor,0)
        
        return resultado
        
    
##Hacemos esta funcion auxiliar que nos servirá para eliminar los 0 que nos sobran
def eliminarceros(lista):
    
    i = len(lista)-1
    
    while True:
        if(lista[i]==0):
            eliminamos=lista.pop(i)
            i-=1
            if(i==-1):
                return []
        else:
            break
    
    return lista
    



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
    
resultado=multiplicacion(polinomio1,polinomio2)


nuevoResultado=eliminarceros(resultado)


impresionPolinomio(nuevoResultado,len(nuevoResultado)-1,len(nuevoResultado)-1,"")