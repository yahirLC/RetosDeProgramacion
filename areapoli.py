"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""
# meti cosas de mas,pero me ayuda a practicar

figuras = ["triangulo", "cuadrado", "rectangulo"]


def area(Figura: str, Ladoa, Ladob: int = 0):

    # aqui hice que la entrada del poligono siempre fuera en minusculas en caso de que el
    # usuario introdusca Triangulo TRIANGULO TriAngulo etc.
    Poligono = Figura.lower()
    print(Poligono)

    if Poligono == str(figuras[0]):
        resultado: int = int(Ladoa) * 3
    elif Poligono == figuras[1]:
        resultado = int(Ladoa) * 4
    elif Poligono == figuras[2]:
        resultado = int(int(Ladoa)*2+int(Ladob)*2)

    if Poligono != "rectangulo":
        print(f"Area de un {Figura} con lado {Ladoa} = {resultado}")
    else:
        print(
            f"Area de un {Figura} con lado {Ladoa} y {Ladob} = {resultado}")


Figura = input("Introduzca el nombre de una figura: ")
Figura = Figura.lower()

try:
    figuras.index(Figura)
except:
    print("Esa figura no esta disponible o no existe")
else:
    if Figura.lower() == "rectangulo":
        lado1 = input("Ingrese el primer lado de la figura: ")
        lado2 = input("Ingrese el segundo lado de la figura: ")
        area(Figura, lado1, lado2)
    else:
        lado1 = input("Introduzca el lado de la figura: ")
        area(Figura, lado1)
