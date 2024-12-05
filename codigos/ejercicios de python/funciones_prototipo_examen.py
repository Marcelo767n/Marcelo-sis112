
def matrix(): #creacion de la matriz 
    matriz=[]
    for i in range(3):
        fila=[]
        for j in range(3):
            num_matrix=float(input(f'ingresa un numero de la columna {j}, de la fila {i} '))
            fila.append(num_matrix)
        matriz.append(fila)
    return matriz
def suma_fil(matriz):
    print('suma de fila')
    filas=len(matriz)
    filasv=[]
    for i in range(filas):
        suma=sum(matriz[i])
        filasv.append(suma)
    print(f' la suma de la filas es {filasv}')
    return filasv
def suma_col(matriz):
    columnas=len(matriz[0])
    columnasv=[]
    filas=len(matriz)
    for i in range(columnas):
        suma=0
        for j in range(filas):
            suma+=(matriz[j][i])
        columnasv.append(suma)
    return columnasv
def suma_total(matriz):
    total=0 
    fila_m=len(matriz)
    for i in range(fila_m):
        total+=sum(matriz[i])   
    return total
        
def minimo(matriz):
    menor=min(min(matriz))
    return menor
def maximo(matriz):
    mayor=max(max(matriz))
    return mayor
    
    

    
        
    
    

    
    