import math

numeroUno = input()

if numeroUno <= 0:
    print("el numero no debe ser menor a cero")
elif numeroUno > 0:
    raiz = math.sqrt(numeroUno)
    cuadrado = math.pow(numeroUno, 2)
    print(raiz,cuadrado)