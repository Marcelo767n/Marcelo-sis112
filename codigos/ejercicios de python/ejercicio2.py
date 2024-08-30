calif=int(input("ingrese el numero de calificaciones "))#ingresa el numero de calificaciones
nota=0
for i in range(calif):
    notas_estudiantes=int(input(f"ingrese la nota {i+1} "))
    print(notas_estudiantes)
    nota=nota+notas_estudiantes
promedio=nota/calif
print (nota)
print(f"el promedio es {promedio} ")