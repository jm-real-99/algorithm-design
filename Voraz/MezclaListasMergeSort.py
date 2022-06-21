################################
###JUAN MANUEL REAL DOMÍNGUEZ###
################################

def voraz(lista):
    ops=0 #Variable acumuladora del número de operaciones
    # Simulamos un do-while
    while(True):
        #Si hemos obtenido una lista de tam=1 es que hemos unido todas las sublistas en una única. Terminamos
        if(len(lista)==1):
            break
        #Si no, entonces seguimos operando
        else:
            #Sumamos las dos primeras listas en una
            v0 = lista.pop(0)
            lista[0]+=v0
            #Contamos las operaciones
            ops += lista[0]
            #Ordenamos la lista para en la próxima iteración trabajar con la lista más pequeña y así
            #realizar un número mínimo de pasos.
            lista.sort()

    return ops


n =int(input(""))
v=(input("")).split(" ")
tams=[]
for i in range(n):
    tams.append(int(v[i]))

#Ordenamos la lista resultante para simplificar los cálculos
tams.sort()

print(voraz(tams))

#4
#8 5 7 4
