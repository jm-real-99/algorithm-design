################################
###JUAN MANUEL REAL DOMÍNGUEZ###
################################
def ordenar(vector, inicio, final, profundidad):
    if inicio == final:
        if vector[inicio]%2 == 0 :
            return [vector[inicio]]
        else:
            return [vector[inicio]]
    elif(final-inicio==1):
        if(vector[inicio]%2==vector[final]%2): #AMBOS SON PARES O IMPARES
            if(vector[inicio]<vector[final]):
                return [vector[inicio],vector[final]]
            else:
                return [vector[final], vector[inicio]]
        elif vector[inicio]%2==0: #vector[inicio] PAR Y EL OTRO IMPAR.
            return [vector[final], vector[inicio]]
        else:
            return [vector[inicio], vector[final]]

    else:
        mitad = (final-inicio)//2

        vmen = ordenar(vector, inicio, inicio+mitad, profundidad+1)
        vmay = ordenar(vector, inicio+mitad+1, final, profundidad+1)
        r=[]

        while( (len(vmen) > 0 and vmen[0]%2!=0) or ( len(vmay) > 0 and vmay[0]%2!=0) ): #Primero van los impares, así que vamos a ordenarlos primero
            if(len(vmen) <= 0 or vmen[0]%2==0): #Si hemos llegado a los pares de vmen, es que hemos acabado los impares de este. Introducimos el resto de vmay.
                r.append(vmay.pop(0))
            elif(len(vmay) <= 0 or vmay[0]%2==0): #Si hemos llegado a los pares de vmay, es que hemos acabado los impares de este. Introducimos el resto de vmen.
                r.append(vmen.pop(0))
            elif(vmen[0] < vmay[0]): #Aún quedan impares de vmen y vmay. Además la cabeza de vmen es menor que la de vmay
                r.append(vmen.pop(0))
            else: #Aún quedan impares de vmen y vmay. Además la cabeza de vmay vmen es menor que la de vmen
                r.append(vmay.pop(0))
        #Ahora solo nos quedan los pares, que estarán hasta que el vector se vacíe.
        while (len(vmen) > 0) or (len(vmay) > 0):  # Mientras que haya elementos en los vectores...
            if len(vmen) == 0:  # Si ya no quedan elementos en el vector menor, añadimos los restantes del mayor
                r.append(vmay.pop(0))
            elif len(
                    vmay) == 0:  # Si ya no quedan elementos en el vector mayor, entonces añadimos los restantes del mayor
                r.append((vmen.pop(0)))
            elif vmen[0] < vmay[0]:
                r.append(vmen.pop(0))
            else:
                r.append(vmay.pop(0))

        return r


def imprimirVector(vector):
    for i in range(len(vector)-1):
        print(str(vector[i]),end=" ")
    print(vector[len(vector)-1])

n =int(input(""))
v=(input("")).split(" ")

numeros=[]
for i in range(n):
    numeros.append(int(v[i]))

resultado = ordenar(numeros,0,len(numeros)-1,0)

imprimirVector(resultado)
