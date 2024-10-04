import random
def generarlist(tamanio_lista ,valorminimo,valormaximo,lista):
    for i in range(tamanio_lista):
        aleatorio=random.randint(valorminimo, valormaximo)
        print(aleatorio)
        lista.append(aleatorio)
    return lista
def encontratar_numero(lista, numero):
    for i in range(len(lista)):
        if (numero==lista[i]):
            print(f'tu numero esta en la posicion: {i} ')
            return 1 # si retorna un 1 encontro el numero  
        else:
            print('el numero no existe ')
            return -1 
            
def busqueda_binaria(lista, numero):
    izquierda, derecha = 0, len(lista)-1
    while izquierda<= derecha:
        medio=(izquierda+derecha)//2
        if lista[medio]==numero:
            return medio 
        elif lista[medio]<numero:
            izquierda=medio+1
        else:
            derecha = medio-1
    return -1 
