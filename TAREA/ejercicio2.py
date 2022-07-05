def cantidad_vocales_a(palabra):
    cant = 0
    for x in range(len(palabra)):
        if palabra[x] == "a" or palabra[x] == "A":
                cant = cant + 1
    return cant

#BloquePrincipal
palabra = input("Ingrese una palabra: ")
print("La palabra", palabra, "Tiene", cantidad_vocales_a(palabra), "a")