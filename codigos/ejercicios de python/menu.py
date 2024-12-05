# main.py

import notas

def mostrar_menu():
    print("\n==== SISTEMA DE GESTIÓN DE NOTAS ====")
    print("1. Agregar nota")
    print("2. Eliminar nota")
    print("3. Modificar nota")
    print("4. Mostrar todas las notas")
    print("5. Calcular promedio")
    print("6. Obtener nota máxima y mínima")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nota = float(input("\n--- AGREGAR NOTA ---\nIngresa la nota: "))
            notas.agregar_nota(nota)

        elif opcion == '2':
            indice = int(input("\n--- ELIMINAR NOTA ---\nIngresa el índice de la nota a eliminar (1 para la primera nota, 2 para la segunda, etc.): ")) - 1
            notas.eliminar_nota(indice)

        elif opcion == '3':
            indice = int(input("\n--- MODIFICAR NOTA ---\nIngresa el índice de la nota a modificar (1 para la primera nota, 2 para la segunda, etc.): ")) - 1
            nueva_nota = float(input("Ingresa la nueva nota: "))
            notas.modificar_nota(indice, nueva_nota)

        elif opcion == '4':
            notas.mostrar_notas()

        elif opcion == '5':
            notas.calcular_promedio()

        elif opcion == '6':
            notas.obtener_max_min()

        elif opcion == '7':
            print("\nSaliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor elige una opción correcta.")

if __name__ == "__main__":
    main()
