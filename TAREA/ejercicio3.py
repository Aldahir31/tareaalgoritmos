def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

#BloquePrincipal
print("Primer Rectangulo")
lado1 = int(input("Ingrese El Lado menor del Rectangulo: "))
lado2 = int(input("Ingrese El Lado mayor del Rectangulo: "))
print("Segundo Rectangulo")
lado3 = int(input("Ingrese El Lado menor del Rectangulo: "))
lado4 = int(input("Ingrese El Lado mayor del Rectangulo: "))
if retornar_superficie(lado1, lado2) == retornar_superficie(lado3, lado4):
    print("Los dos Rectangulos Tienen la Misma Superficie")
else:
    if retornar_superficie(lado1, lado2) > retornar_superficie(lado3, lado4):
        print("El Primer Rectangulo Tiene una Superficie Mayor")
    else:
        print("El Segundo Rectangulo Tiene una Superficie Mayor")