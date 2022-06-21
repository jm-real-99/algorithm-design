# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:36:47 2021

@author: Usuario
"""

def ejer2(n):
    if(n<=0):
        return 0
    else:
        n=n/10
        return 1+ejer2(int(n))

num = input ("Dame un numero")
int(num)
print ("n=",num)
print (type(num))
resultado = ejer2(int(num))

print("RESULTADO:",resultado)