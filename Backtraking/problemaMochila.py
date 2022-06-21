################################
###JUAN MANUEL REAL DOMÍNGUEZ###
################################

#objetos: Será el array del peso de todos los objetos
#mochilas: Array de tam 2, que indica el peso total de las dos mochilas
#usados: Array booleano de tam=objetos. Indicamos si el de la misma posición del array objeto está metido en alguna mochila.
#tam: Int que indica el tamaño del array de objetos
#maximo: Int. Indica el tamaño máximo que hemos podido almacenar hasta el momento.
#peso: Int. Variable acumuladora, indicará el peso que llevamos cargado en la mochila.

def CalcularPesos(objetos,mochilas,peso,pos,tam,maximo):

    i=0
    while i<3 :
        if (pos == tam - 1):  # Si somos la última iteración, osea, el último objeto de la lista
            pesoTotal = peso[0] + peso[1]  # Peso que llevamos en ambas mochilas
            if (peso[0] + objetos[pos] <= mochilas[0]):  # Vemos si cabemos en la mochila 0
                if(pesoTotal+objetos[pos]>maximo):
                    maximo=pesoTotal+objetos[pos]

            elif (peso[1] + objetos[pos] <= mochilas[1]):
                if (pesoTotal + objetos[pos] > maximo):
                    maximo = pesoTotal + objetos[pos]

            else:  # Entonces no cabemos en ninguna mochila
                if (pesoTotal > maximo):
                    maximo = pesoTotal

        else:
            if(i==0): #Si i==0 es que el objeto va a ir en la mochila 0
                if(peso[0]+objetos[pos]<=mochilas[0]): #Si aún cabe en la mochila 0
                    peso[0]+=objetos[pos]
                    maximo = CalcularPesos(objetos, mochilas, peso, pos+1, tam, maximo)
                    #Estamos aquí, eso es que el objeto no va a ir en la mochila 0
                    peso[0] -= objetos[pos]
            elif(i==1): #Si i==1 es que el objeto va a ir en la mochila 1
                if (peso[1] + objetos[pos] <= mochilas[1]):  # Si aún cabe en la mochila 0
                    peso[1] += objetos[pos]
                    maximo =CalcularPesos(objetos, mochilas, peso, pos + 1, tam, maximo)
                    peso[1] -= objetos[pos]
            else: #Entonces el objeto no va en ninguna mochila
                maximo = CalcularPesos(objetos, mochilas, peso, pos + 1, tam, maximo)

        i+=1

    return maximo





n =int(input(""))
v=(input("")).split(" ")
m=(input("")).split(" ")
productos = []
mochilas=[]
mochilas.append(int(m[0]))
mochilas.append(int(m[1]))
for i in range(n):
    productos.append(int(v[i]))

maxim = CalcularPesos(productos,mochilas,[0,0],0,n,0)

print(maxim)