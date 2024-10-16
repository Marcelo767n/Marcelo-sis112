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