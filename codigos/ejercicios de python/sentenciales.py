n = int(input("ingrese un numero").strip())
if n % 2 == 1:
            print("Weird")
else:
    if n>=2:
        if n<=5:
            print ("Not Weird")
        elif n>=6:
            if n<=20:
                print("Weird")
            elif n>20:
                print ("Not Weird")  

