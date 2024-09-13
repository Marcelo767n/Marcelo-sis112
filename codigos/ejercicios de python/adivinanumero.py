import random
print('Adivina el Numero')
print('estoy pensando en numero entre 1 y 100, adivina en que numero estoy pensando ')
num=random.randint(1, 100)
intentos=0
while True:
    intentos += 1
    numero=int(input('ingrese un numero '))
    if numero>num: 
        print ('demasiado alto intenta de nuevo')
    elif numero<num:
        print ('demasiado bajo intenta de nuevo')    
    elif num==numero:
        print('ganaste el juego')
        break
    else:
        print ('por favor introduce un numero valido ')
    print (f'numero de intento: {intentos}')
    