"""/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
 """

todomorse = {"a": ".-",
             "b": "-...",
             "c": "-.-.",
             "d": "-..",
             "e": ".",
             "f": "..-.",
             "g": "--.",
             "h": "....",
             "i": "..",
             "j": ".---",
             "k": "-.-",
             "l": ".-..",
             "m": "--",
             "n": "-.",
             "o": "---",
             "p": ".--.",
             "q": "--.-",
             "r": ".-.",
             "s": "...",
             "t": "-",
             "u": "..-",
             "v": "...-",
             "w": ".--",
             "x": "-..-",
             "y": "-.--",
             "z": "--..",
             " ": " "}

entrada = input("Ingrese texto a convertir: ")

todomorse_inverso = dict(zip(todomorse.values(), todomorse.keys()))

conversion = list()
final = ""

if entrada[0] == "." or entrada[0] == "-":
    entrada = entrada.split()
    for signo in entrada:
        final = final+todomorse_inverso.get(signo)+""
    print(final)

else:
    for letra in entrada:
        final = final+todomorse.get(letra)+" "
    print(final)
