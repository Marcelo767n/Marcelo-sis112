import funciones_busqueda as fb 
import time 
lista_aleatoria=[]
lista_personalizada=[]
def menu():
    print("""Bienvenido al menu de busqueda
                ___Opciones___

1. Crear una lista personalizada de n números
2. Crear una lista aleatoria de n números sin repetidos
3. Buscar un número en la lista usando búsqueda lineal
4. Buscar un número en la lista usando búsqueda binaria
5. Descomponer un número en sus dígitos usando recursión
6. Salir""" )

    

while True:
    menu()
    opcion=int(input('ingresa una opcion: '))
    if opcion==1:
        lista_p=[]
        tamanio_lista_p=int(input('ingrese el tamaño de la lista '))
        lista_personalizada=fb.lista_p(tamanio_lista_p, lista_p) 
        print(lista_p)
    elif opcion==2:
        lista_a=[]
        tamanio_lista_a=int(input('ingrese el tamaño de la lista '))
        valormin=int(input('ingrese el valor minimo de la lista aleatoria '))
        valormax=int(input('ingrese el valor maximo de la lista aleatoria '))
        lista_aleatoria=fb.lista_a(tamanio_lista_a, lista_a, valormin, valormax)
        print(lista_a)
    elif opcion==3:
        if not lista_personalizada and not lista_aleatoria: #si no hay lista personalizada  ni lista aleatoria no se puede pasar a la opcion 3 
            print('primero debes crear una lista ')
            continue
        print("""escoge la lista de la cual buscar el numero
                  a) lista personalizada
                  b) lista aleatoria """)
        inciso=str(input('ingresa un inciso '))
        if inciso=='b':
                    num=float(input('ingresa el numero que desear buscar '))
                    tiempo_inicio=time.time()
                    fb.busqueda_lineal(lista_aleatoria,num)
                    tiempo_fin=time.time()
                    print(f'el tiempo que tardo la busqueda es: {(tiempo_fin-tiempo_inicio)*1000000} micro segundos')
        elif inciso=='a':
                    num=float(input('ingresa el numero que desear buscar '))
                    tiempo_inicio=time.time()
                    fb.busqueda_lineal(lista_personalizada,num)
                    tiempo_fin=time.time()
                    print(f'el tiempo que tardo la busqueda es: {(tiempo_fin-tiempo_inicio)*1000000} micro segundos')
    elif opcion==4:
            if not lista_personalizada and not lista_aleatoria:
                print('primero debes crear una lista ')
                continue
            print("""escoge la lista de la cual buscar el numero
                  a) lista personalizada
                  b) lista aleatoria """)
            inciso=str(input('ingresa un inciso: '))
            if inciso=='a':
                    num=float(input('ingresa el numero que desear buscar: '))
                    tiempo_inicio=time.time()
                    lista_ordenada=fb.ord_burbuja(lista_personalizada)
                    tiempo_fin=time.time()
                    print(f'el tiempo que tardo la busqueda es: {(tiempo_fin-tiempo_inicio)*1000} ms')
                    tiempo_inicio=time.time()
                    fb.busqueda_binaria(lista_ordenada,num)
                    tiempo_fin=time.time()
                    print(f'el tiempo que tardo la busqueda es: {(tiempo_fin-tiempo_inicio)*1000000000} pico segundos')
            elif inciso=='b':
                    num=float(input('ingresa el numero que desear buscar: '))
                    tiempo_inicio=time.time()
                    lista_ordenada=fb.ord_burbuja(lista_aleatoria)
                    tiempo_fin=time.time()
                    print(f'el tiempo que tardo la busqueda es: {(tiempo_fin-tiempo_inicio)*1000} ms')
                    tiempo_inicio=time.time()
                    fb.busqueda_binaria(lista_ordenada,num)
                    tiempo_fin=time.time()
                    print(f'el tiempo que tardo la busqueda es: {(tiempo_fin-tiempo_inicio)*1000000000} pico segundos')
    elif opcion==5:
        num_descomponer=int(input('ingresa el numero que deseas descomponer '))
        print(fb.descomponer_numero(num_descomponer))
    elif opcion==6:
        break
    else:
        print('selecciona una opcion correcta ')
        
        
                        
                
        
        


