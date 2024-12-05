import funciones_prototipo_examen
def menu():
    print('primero creemos la matriz')
   
    print('ahora que quieres realizar con la matriz ')
    print('1.- suma de filas ')
    print('2.- suma de columnas ')
    print('3.- suma total de los componentes de la matriz ')
    print('4.- hallar el valor minimo de la matriz')
    print('5.- hallar el valor maximo de la matriz')
    print('6.- salir')
while True:
    matriz=funciones_prototipo_examen.matrix()
    print('tu matriz es:')
    for i in matriz:
        print(i)
    opciones=int(input(' selecciona una opcion '))
    if opciones==1:
        print(f"el resultado de la suma de las filas es: {funciones_prototipo_examen.suma_fil(matriz)}")
    elif opciones==2:
        print(f'el resultado de la suma de las columnas es: {funciones_prototipo_examen.suma_col(matriz)}')
    elif opciones==3:
        print(f'el resultado de la suma total de la matriz es: {funciones_prototipo_examen.suma_total(matriz)}')
    elif opciones==4:
        print(f"el valor minimo de la matriz es: {funciones_prototipo_examen.minimo(matriz)}")
    elif opciones==5:
        print(f"el valor maximo de la matriz es: {funciones_prototipo_examen.maximo(matriz)}")
    elif opciones==6:
        print('saliste')
        break
    else:
        print('seleccione una opcion correcta')
