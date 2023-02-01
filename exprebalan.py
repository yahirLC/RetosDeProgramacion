"""
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""


def mostrarbalanceo(simbolo1: str, tipo: str):
    if simbolo1 == "{":
        if tipo == "b":
            print("Llaves balanceadas")
        elif tipo == "d":
            print("Llaves desvalanceadas")

    elif simbolo1 == "[":
        if tipo == "b":
            print("Corchetes balanceados")
        elif tipo == "d":
            print("Corchetes desvalanceados")

    else:
        if tipo == "b":
            print("Parentesis balanceados")
        elif tipo == "d":
            print("Parentesis desvalanceados")


def balanceado(simbolo1: str, simbolo2: str, texto1: list):
    if texto1.count(simbolo1) == texto1.count(simbolo2) != 0:
        mostrarbalanceo(simbolo1, "b")
    elif texto1.count(simbolo1) == 0 and texto1.count(simbolo2) == 0:
        return
    else:
        mostrarbalanceo(simbolo1, "d")


def verificador(texto: str):
    # parentesis comprobacion
    formula = ""

    for signo in texto:
        if signo == "{" or signo == "}":
            formula = formula+signo
        elif signo == "[" or signo == "]":
            formula = formula+signo
        elif signo == "(" or signo == ")":
            formula = formula+signo

    print(formula)

    balanceado("{", "}", texto)
    balanceado("[", "]", texto)
    balanceado("(", ")", texto)


entrada = input("Ingrese la expresion: ")
verificador(entrada)
