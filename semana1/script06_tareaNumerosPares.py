def numeros_pares(cadena):
    posicion = 0
    for letra in cadena:
        if posicion % 2 == 0:
            print(cadena[posicion], posicion)
        posicion = posicion + 1

numeros_pares("supercalifragilisticoespiralidoso")
