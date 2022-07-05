def retornar_perimetro(lado):
    return lado*4

#BloquePrincipal
lado = int(input("Ingrese el Lado del Cuadrado: "))
x = retornar_perimetro(lado)
print("El Perimetro del cuadrado es", x)
