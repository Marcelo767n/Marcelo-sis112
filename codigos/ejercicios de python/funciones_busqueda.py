import random

def lista_p(tamanio_lista, lista):
    
    for i in range(tamanio_lista):
        print(f'Tu lista tiene {tamanio_lista} elementos ')
        while True:
            
            num = float(input(f'Ingresa el número {i+1} de la lista: '))
            if num not in lista:  
                lista.append(num)
                break  
            else:
                print(f"El número {num} ya está en la lista. Ingresa otro número.")

    return lista
def lista_a(tamanio_lista, lista, valorminimo, valormaximo):
    print(f'Tu lista tiene {tamanio_lista} elementos ')
    for i in range(tamanio_lista):
        while True:
            
            aleatorio=random.randint(valorminimo, valormaximo)
            if aleatorio not in lista:  
                lista.append(aleatorio)
                break  
    return lista 
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
    
    return lista
def busqueda_lineal(lista, numero):
    for i in range(len(lista)):
        if (numero==lista[i]):
            print(f'tu numero esta en la posicion: {i} ')
def busqueda_binaria(lista, objetivo):
    inicio=0
    fin = len(lista)
    while inicio<= fin:
        medio = (inicio+fin)//2
        if lista[medio]==objetivo:
            return medio 
        elif lista[medio]< objetivo:
            inicio=medio + 1
        else:
            fin=medio -1 
    return -1