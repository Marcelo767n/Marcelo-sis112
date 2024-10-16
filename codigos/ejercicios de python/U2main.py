from xml.dom import InvalidModificationErr
import u2_funcniones as tarea
import time 
listanum=[]
listacomp=int(input("cuanto sera el rango de num que quiere generar?.."))
minnum=int(input("cual sera el valor min del rango.."))
maxnum=int(input("cual sera el valor max del rango.."))
inicio=time.time()
tarea.generarlist(listacomp,minnum,maxnum,listanum)
fin=time.time()
print(f'tiempo transcurrido de la generacion de la lista \n {(fin-inicio)*1000}')

print(len(listanum))
print(type(listanum))
print("""seleccione una opcion de ordenamiento
      opcion 1 busqueda lineal
      opcion 2 busqueda binaria 
      opcion 3 ordenamiento de lista burbuja""")
opcion=int(input('seleccione una opcion de algoritmo de busqueda u ordenamimiento'))
if opcion==1:    
    num_encontrar=int(input('ingrese el numero a encontrar '))
    inicio=time.time()
    tarea.encontratar_numero(listanum,num_encontrar)
    fin=time.time()
    print(f'tiempo transcurrido de la generacion de la lista lineal \n {(fin-inicio)*1000}')
elif opcion==2:
    listaordn=sorted(listanum)
    num_encontrar2=int(input('ingrese un numero a encontrar de la lista'))
    inicio=time.time()
    tarea.busqueda_binaria(listaordn,num_encontrar2)
    fin=time.time()
    print(f'tiempo transcurrido de la generacion de la lista binario \n {(fin-inicio)*1000}')
elif opcion==3:
    tarea.ord_burbuja(listanum)
    print('la lista ordenada es:\n', listanum)