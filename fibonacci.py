"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

penultimo = 1
ultimo = 0
numero = 0
i = 0

while (i < 50):

    print(numero)
    numero = penultimo + ultimo
    penultimo = ultimo
    ultimo = numero

    i = i+1
