################################
###JUAN MANUEL REAL DOMÍNGUEZ###
################################
import math
import numpy as np
import matplotlib.pyplot as plt

#FÓRMULA PUNTO MEDIO:
#
# M= ( ((x1+x2)/2) , ((y1+y2)/2) )
#
def calculoPuntoMedio(x1,x2,y1,y2):
    xr = (x1+x2)/2
    yr = (y1+y2)/2

    return [xr,yr]

def dibujarFractal(verticesX,verticesY,nivel):
    if(nivel==0): #CASO BASE, NO HACEMOS NADA. NOS SERVIRÁ PARA NO LLAMAR MÁS RECURSIVAMENTE Y SABER CUANDO ACABAR.
        None
    else:
        #Primero vamos a sacar la mitad de cada lado. Lo haremos utilizando los vértices
        vxr=[]
        vyr=[]
        for i in range(3):
            ii = (i+1)%3
            pr=calculoPuntoMedio(verticesX[i],verticesX[ii],verticesY[i],verticesY[ii])
            vxr.append(pr[0])
            vyr.append(pr[1])
        #Ahora vamos a obtener los 3 triángulos contenidos en el actual. Lo haremos en sentido horario comenzando por el triángulo más abajo a la izquierda.
        t1x = [verticesX[0],vxr[0],verticesX[1]]
        t1y = [verticesY[0],vyr[0],verticesY[0]]
        t2x = [vxr[0],verticesX[1],vxr[1]]
        t2y = [vyr[0],verticesY[1],vyr[1]]
        t3x = [vxr[2],vxr[1],verticesX[2]]
        t3y = [vyr[2],vyr[1],verticesY[2]]

        #Introducimos el primer elemento al final, porque así, a la hora de dibujar el triángulo se hace completamente.
        vxr.append(vxr[0])
        vyr.append(vyr[0])
        # Dibujamos el triángulo dado por los vertices de la mitad. Con eso y el triángulo exterior ya estaremos dibujando los 3 triángulos.
        plt.plot(vxr,vyr)
        #Dividimos el problema recursivamente haciendo el mismo proceso para cada triángulo:
        dibujarFractal(t1x,t1y,nivel-1)
        dibujarFractal(t2x, t2y, nivel - 1)
        dibujarFractal(t3x, t3y, nivel - 1)

def fractal(x):
    #Dibujamos el triángulo base con las siguientes coordenadas (la última es la primera porque plt imprime por puntos y tenemos que cerrar la figura):
    plt.plot([0,0.5,1,0],[0,1,0,0])
    if(x!=0): #Si el nivel dado es 0, no hacemos nada más, si no, entonces llamamos recursivamente a la función de DyV
        dibujarFractal([0,0.5,1],[0,1,0],x)


n =int(input(""))
fig = plt.figure()
fig.patch.set_facecolor("white")
fractal(n)
plt.axis("equal")
plt.axis("off")
plt.show()
