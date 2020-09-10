def crecimiento():
    poblacionA=35.0
    poblacionB=19.9
    iA=0.02
    iB=0.03
    anio=0
    while(poblacionA>poblacionB):
        poblacionA+=poblacionA*iA
        poblacionB+=poblacionB*iB
        anio+=1

    print("La población del país B supera a la de A en el año ",anio)
    return anio


