print("usted esta titulado como bachiller, si=1 o no=2")
bachiller = input()

if bachiller == 1:
    print("usted puede matricularse")
elif bachiller== 2:
    print("usted supero la prueba de acceso, si=1 o no=2")
    examen = input()
    if examen == 1:
        print("usted ahora puede matricularse")
    else:
        print("lo sentimos, puede intentarlo en la siguiente convocatoria")
