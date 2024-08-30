materias=int(input('ingrese el numero de calificaciones '))
notas=[0]
for i in range(materias):
    valor=float(input(f"Ingrese el valor de la nota {i+1}: "))
    notas.append(valor)
    
promedio=sum(notas)/materias
print(f"el promedio es: {promedio}")

