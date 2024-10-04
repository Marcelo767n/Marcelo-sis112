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
print(listanum)
print(len(listanum))
print(type(listanum))

num_encontrar=int(input('ingrese el numero a encontrar '))
inicio=time.time()
tarea.encontratar_numero(listanum,num_encontrar)
fin=time.time()
print(f'tiempo transcurrido de la generacion de la lista \n {(fin-inicio)*1000}')

x=sorted(listanum)
print(x)
