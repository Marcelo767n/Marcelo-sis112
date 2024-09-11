import fun_conversiones

def menu():
    print('1. pasar de metros a kilometros o viceversa ')
    print('2. pasar de gramos a kilogramos o viceversa ')
    print('3. pasar de Celsius o Farenheit o viceversa ')
    print('4 salir')
while True:
    menu()
    opcion=int(input('elige cualquiera de las cuatro opciones '))
    if opcion==4:
        print('usted salio de la calculadora')
        break
    elif opcion>4:
        print('seleccione una opcion correcta')
    num=float(input('ingrese el numero que desea convertir: '))
    
    if opcion==1:
        print(f'Resultado: {fun_conversiones.metros(num)}')
    elif opcion==2:
        print(f'Resultado: {fun_conversiones.masa(num)}')
    elif opcion==3:
        print(f'Resultado: {fun_conversiones.Temp(num)}')

