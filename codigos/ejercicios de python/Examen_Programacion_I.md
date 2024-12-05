
# Examen - Programación I

## Objetivo
Crear un programa en Python que integre los algoritmos de búsqueda y ordenamiento que estudiamos en clase. El programa debe presentar un menú interactivo que permita al usuario realizar distintas operaciones con listas de números.

### Menú del Programa
El menú debe ofrecer las siguientes opciones:

```
1. Crear una lista personalizada de n números
2. Crear una lista aleatoria de n números sin repetidos
3. Buscar un número en la lista usando búsqueda lineal
4. Buscar un número en la lista usando búsqueda binaria
5. Descomponer un número en sus dígitos usando recursión
6. Salir
```

### Descripción de cada opción del menú

1. **Crear una lista personalizada de n números**  
   - El programa debe pedir al usuario cuántos elementos (n) quiere en la lista.
   - Luego, el usuario deberá ingresar cada número uno por uno hasta completar la lista.

2. **Crear una lista aleatoria de n números sin repetidos**  
   - El programa debe pedir al usuario cuántos elementos (n) quiere en la lista.
   - La función debe generar automáticamente una lista con n números aleatorios únicos (sin repetirse).

3. **Buscar un número en la lista usando búsqueda lineal**  
   - Esta opción debe pedir al usuario dos cosas:
     1. El número que desea buscar.
     2. En qué lista buscar el número (lista personalizada o lista aleatoria).
   - **Medición de tiempo:** Usando la biblioteca `time`, el programa debe medir cuánto tiempo tarda la búsqueda lineal en completarse y mostrar ese tiempo en pantalla.

4. **Buscar un número en la lista usando búsqueda binaria**  
   - Esta opción debe pedir al usuario dos cosas:
     1. El número que desea buscar.
     2. En qué lista buscar el número (lista personalizada o lista aleatoria).
   - **Ordenamiento y medición de tiempo:** 
     - Antes de realizar la búsqueda binaria, la lista seleccionada debe ser ordenada, ya que la búsqueda binaria solo funciona en listas ordenadas.
     - El programa debe medir y mostrar dos tiempos de ejecución:
       - El tiempo que toma ordenar la lista.
       - El tiempo que toma realizar la búsqueda binaria en la lista ya ordenada.

5. **Descomponer un número en sus dígitos usando recursión**  
   - Esta opción debe pedir al usuario un número de varios dígitos.
   - Luego, debe usar una función recursiva para descomponer el número en sus dígitos y mostrarlos en una lista.  
   
   **Ejemplo:**  
   ```
   Número a descomponer: 2549
   Salida: [2, 5, 4, 9]
   ```

6. **Salir**  
   - Esta opción debe terminar la ejecución del programa.

### Instrucciones adicionales

- **Estructura del código:**  
  - El código debe estar organizado en dos archivos:
    - Un archivo principal, que ejecuta el menú y el bucle principal.
    - Un archivo de biblioteca, donde estarán todas las funciones creadas para cada opción del menú.

- **Medición de tiempos en las búsquedas:**  
  - Es obligatorio que en la búsqueda lineal y la búsqueda binaria se mida el tiempo de ejecución utilizando la biblioteca `time`.
  - En la búsqueda binaria, se debe medir por separado el tiempo de ordenamiento y el tiempo de la búsqueda.

- **Detalles adicionales:**  
  - El programa debe ser claro en sus instrucciones para el usuario.
  - Asegurarse de que no se repitan los números en la lista aleatoria generada.
