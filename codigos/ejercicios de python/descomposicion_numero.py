def descomponer_numero(n):
    if n < 10:
        return [n]
    else:
        digito_num=descomponer_numero(n//10)
        ultimo_digito=n%10
        return digito_num+[ultimo_digito]
print(descomponer_numero(243567))


def descomp_num(n):
    if n<10:
        return[n]
    else:
        return descomp_num(n//10) + [n%10]

print(descomp_num(154914532495))

def factorial(n):
    resultado=1
    if n==0 or n==1:
        return 1 
    else:
        for i in range(1, n + 1):  # Iteramos desde 1 hasta n
            resultado *= i  # Multiplicamos el resultado por i en cada iteración
    return resultado  # Retornamos el resultado final
print(factorial(10))

def fibonacci(n):
    if n == 0:
        return 0  # Caso base: fibonacci(0) = 0
    elif n == 1:
        return 1  # Caso base: fibonacci(1) = 1
    
    a, b = 0, 1  # Inicializamos los dos primeros números de Fibonacci
    for i in range(2, n + 1):  # Empezamos desde 2 hasta n
        a, b = b, a + b  # Actualizamos a y b: b se convierte en el siguiente número de Fibonacci
    return b  # Retornamos el último número calculado

print(fibonacci(10))