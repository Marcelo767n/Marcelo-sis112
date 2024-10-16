import random
def generarlist(tamanio_lista ,valorminimo,valormaximo,lista):
    for i in range(tamanio_lista):
        aleatorio=random.randint(valorminimo, valormaximo)
        if aleatorio not in lista:
            lista.append(aleatorio)
            print(aleatorio)
    print(f"el tamano de la lista es: {len(lista)}")
    return lista
def encontratar_numero(lista, numero):
    for i in range(len(lista)):
        if (numero==lista[i]):
            print(f'tu numero esta en la posicion: {i} ')
            return 1 # si retorna un 1 encontro el numero  
        else:
            print('el numero no existe ')
            return -1 
            

def busqueda_binaria(lista, objetivo):
    inicio=0
    fin = len(lista)
    while inicio<= fin:
        medio = (inicio+fin)//2
        print("======\n", medio)
        if lista[medio]==objetivo:
            return medio 
        elif lista[medio]< objetivo:
            inicio=medio + 1
        else:
            fin=medio -1 
        print(medio)
    return -1
#Algoritmo para ordenar listas 
def ord_burbuja(lista): # algoritmo de ordenamiento burbuja
    n= len(lista)
    #recorre toda la lista 
    for i in range(n):
        # ultimos i elementos ya estan ordenadas 
        for j in range (0, n-i-1):
            # intercambia si el elemento actual es mayor que el siguiente 
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
    
    return lista
        


