def metros(a):
    print('1. de metros a kilometros')
    print('2. de kilometros a metros')
    n=int(input('seleccione una opcion '))
    if n==1: #seleccione una de las dos opciones para realizar operaciones
        return a/1000
    elif n==0:
        return a*1000
    else:
        print('selecciona una opcion correcta')
def masa(a):
    print('1. de gramos a kilogramos')
    print('2. de kilogramos a gramos')
    n=int(input('seleccione una opcion '))
    if n==1: #seleccione una de las dos opciones para realizar operaciones
        return a/1000
    elif n==2:
        return a*1000
    else:
        print('selecciona una opcion correcta')
def Temp(a):
    print('1. de Celsius a Farenheit')
    print('2. de Farenheit a Celsius')
    n=int(input('seleccione una opcion '))
    if n==1: #seleccione una de las dos opciones para realizar operaciones
        return (a*1.8)+32
    elif n==2:
        return (a-32)/1.8
    else:
        print('selecciona una opcion correcta')

        
        
    