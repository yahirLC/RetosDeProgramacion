"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""
# instale colorama para mostrar los numeros primos y no primos por color
# comando para instalar colorama: python -m pip install colorama

# aqui hay mas informacion de colorama : https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/

# aqui importe una constante llamada fore y le puse el nombre de color para que sea mas memorable para mi
from colorama import Fore as color, init
init()


def primo(numero: int):
    if numero == 2 or numero == 3 or numero == 5 or numero == 7:
        print(color.RED+f"{numero} "+"Primo"+color.RESET)
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        print(color.GREEN+f"{numero} "+"No primo"+color.RESET)
    else:
        print(color.RED+f"{numero} "+"Primo"+color.RESET)


numero = 1

while (numero <= 100):
    primo(numero)
    numero = numero+1
