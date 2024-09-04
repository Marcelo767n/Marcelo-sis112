num_estudiantes = int(input("Ingrese el número de estudiantes: "))
num_notas = int(input("Ingrese el número de notas por estudiante: "))

matrizdenotas=[]
for i in range(num_estudiantes):
    print(f'ingrese el numero de notas del estudiante  {i+1} ')
    notas=[]
    for j in range(num_notas):
        nota=float(input(f'ingrese la nota {j+1} '))
        notas.append(nota)
    matrizdenotas.append(notas)
print(matrizdenotas)

for k in range (num_estudiantes):
    promedio=sum(matrizdenotas[k])/num_notas
    print(f'estudiante {k+1}, promedio: {promedio} ')