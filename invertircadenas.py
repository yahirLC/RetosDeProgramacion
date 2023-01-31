"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

texto = input(str("Ingresa un texto: "))
i = len(texto)
x = 0
lista = list()

while x != i:
    lista.append(texto[x])
    x = x+1

inversa = list()

while i != 0:

    inversa.append(lista[i-1])
    i = i-1

textoinverso = "".join(inversa)
print(textoinverso)
