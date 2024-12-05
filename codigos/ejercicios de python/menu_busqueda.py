from sympy import true
import funciones_busqueda as fb
import time

print('menu de busqueda y ordenamiento las opciones son: ')
print('creacion de lista propia: ')
#lista_c=[]
tamano_lista=int(input('ingrese el tamano que tendra la lista '))
#lista_propia=fb.lista_p(tamano_lista, lista_c)
#print(lista_propia)
print('creacion de lista aleatoria ')
lista_al=[]
min=int(input('ingrese el rango minimo que tendra la lista aleatoria '))
max=int(input('ingrese el rango maximo que tendra la lista aleatoria '))
lista_aleatoria=fb.lista_a(tamano_lista, lista_al, min, max)
print(lista_aleatoria)
print(""" Opciones:
      1. busqueda lineal
        a. en lista creada aleatoriamente
        b. en lista propia
      2. busqueda binaria 
        a. en lista creada aleatoriamente 
        b. en lista propia
        c. con ordenamietno burbuja en lista creada aleatoriamente 
        d.  con ordenamiento burbuja en lista propia
      3. ordenamiento burbuja
        a. en lista creada aleatoriamente 
        b. en lista propia """)


while True:
    opcion=int(input('ingrese la opcion que desea realizar '))
    if opcion==1:
        inciso=str(input('escoge un inciso entre a o b '))
        if inciso=='a':
            num_encontrar=int(input(' ingrese el numero que desea buscar en la lista aleatoria '))
            tiempo_inicio=time.time()
            fb.busqueda_lineal(lista_aleatoria, num_encontrar)
            tiempo_fin=time.time()
            print(f"""el tiempo de ejecucion para la lista aleatoria con busqueda lineal 
              es: {(tiempo_fin-tiempo_inicio)*1000} ms """)
        elif inciso=='b':
            num_encontrar2=int(input(' ingrese el numero que desea buscar en la lista propia '))
            #tiempo_inicio=time.time()
            #fb.busqueda_lineal(lista_propia,  num_encontrar2)
            #tiempo_fin=time.time()
            #print(f"""el tiempo de ejecucion para la lista  propia con busqueda lineal
            #       es: {(tiempo_fin-tiempo_inicio)*1000} ms """)
    elif opcion==2:
        num_encontrar=int(input(' ingrese el numero que desea buscar en la lista aleatoria '))
        tiempo_inicio=time.time()
        lista_ord1=fb.ord_burbuja(lista_aleatoria)
        fb.busqueda_binaria(lista_ord1, num_encontrar)
        tiempo_fin=time.time()
        print(f""" el tiempo de ejecucion para la lista aleatoria con busqueda binaria
              y ordenamiento burbuja es {(tiempo_fin-tiempo_inicio)*1000} ms""")
        #num_encontrar2=int(input(' ingrese el numero que desea buscar en la lista propia '))
        #tiempo_inicio=time.time()
        #lista_ord2=fb.ord_burbuja(lista_propia)
        



        

        
    