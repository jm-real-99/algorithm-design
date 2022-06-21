# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:22:25 2021

@author: Juan Manuel Real
"""
import math #Esta librería nos simplificará el calculo del valor absoluto

ERROR=0.000001 #Variable global del error permitido (10^-6)

def newtonRaphson (x,a):
    
    f=(x**2)-a #Guardamos en f la funcion que sería f(x)=x^2-a
    fprim=2*x #Guardamos en fprim la funcion f(x) derivada, que sería fprim(x)=2*x
    absoluto= math.fabs(f) #Guardamos en una variable el valor absoluto de f, que nos servirá para comprobar si hemos llegado a la solucion aproximada
   
    #Comprobamos si hemos terminado
    if(absoluto<=ERROR):
        return x
    
    #Si no hemos terminado, entonces reducimos el problema recursivamente, pasando como nueva x siendo x', con el calculo:
    #x' = x-(f(x)/f'(x))
    else:
        return newtonRaphson(x-(f/fprim),a)
    
a=float(input(""))
print(" %.4f" %newtonRaphson(a,a))
