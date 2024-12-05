# notas.py

# Lista donde se almacenarán las notas
notas = []

def agregar_nota(nota):
    if 0 <= nota <= 100:
        notas.append(nota)
        print("Nota agregada exitosamente.")
    else:
        print("Error: La nota debe estar en el rango de 0 a 100.")

def eliminar_nota(indice):
    try:
        notas.pop(indice)
        print("Nota eliminada exitosamente.")
    except IndexError:
        print("Error: Índice fuera de rango.")

def modificar_nota(indice, nueva_nota):
    try:
        if 0 <= nueva_nota <= 100:
            notas[indice] = nueva_nota
            print("Nota modificada exitosamente.")
        else:
            print("Error: La nota debe estar en el rango de 0 a 100.")
    except IndexError:
        print("Error: Índice fuera de rango.")

def mostrar_notas():
    if notas:
        print("\n--- LISTA DE NOTAS ---")
        for i, nota in enumerate(notas, start=1):
            print(f"Nota {i}: {nota}")
    else:
        print("No hay notas registradas.")

def calcular_promedio():
    if notas:
        promedio = sum(notas) / len(notas)
        print(f"\nEl promedio de las notas es: {promedio:.2f}")
    else:
        print("No hay notas para calcular el promedio.")

def obtener_max_min():
    if notas:
        max_nota = max(notas)
        min_nota = min(notas)
        print(f"\nNota máxima: {max_nota}")
        print(f"Nota mínima: {min_nota}")
    else:
        print("No hay notas registradas.")
