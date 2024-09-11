def año_bisiesto(año):
    if año%4==0:
        if año%100==0:
            if año%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
for year in range(1900):
    año=int(input("ingrese eñ año"))
    resultado=año_bisiesto(año)
