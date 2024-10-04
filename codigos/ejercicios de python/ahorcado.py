import random
def obtener_palabra():
    palabras=['perro','marciano','programacion','computadora']
    palabra_aleatoria=(random.choice(palabras))
    return palabra_aleatoria

def tablero(palabra_secreta,letras_adivinadas):
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_"
            
    print(tablero)

def ahorcado():
    palabra_secreta=obtener_palabra()
    letra_adivinadas=[]
    intentos=5
    
    while intentos>0:
        tablero(palabra_secreta, letra_adivinadas)
        letra=input('introduce una letra ').lower()
        if letra in letra_adivinadas:
            print('ya introduciste la letra ')
            continue
        if letra in palabra_secreta:
            letra_adivinadas.append(letra)
            if set(letra_adivinadas)==set(palabra_secreta):#se utiliza la funcion set para comparar
                print('ganaste')
                break
        else:
            intentos-=1
            print(f'letra incorrecta te quedan {intentos}')
    if intentos==0:
        print(f"has perdido, la pablabra secreta era: {palabra_secreta}")                

ahorcado()             
    
    


    
    
    

    
    

