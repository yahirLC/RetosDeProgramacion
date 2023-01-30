"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""


def recibir(palabra1: str, palabra2: str):

    # SORTED() LO QUE HACE SORTED ES TOMAR LOS CARACTERES PARA LUEGO ORDENARLOS ALFABETICAMENTE

    if sorted(palabra1) == sorted(palabra2):
        return True


valor = recibir("amlo", "loma")
print(type(valor))
