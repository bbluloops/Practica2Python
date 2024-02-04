"""Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
- Input: Twitter Output: Twttr
- Input: What's your name? Output: Wht's yr nm?
"""

def omitir_vocales(cadena):
    traduccion = str.maketrans("", "", "AEIOUaeiou")
    resultado = cadena.translate(traduccion)
    return resultado

cadena_ingresada = input("Ingrese una cadena de texto: ")

resultado_omitir_vocales = omitir_vocales(cadena_ingresada)
print(f"Texto con vocales omitidas: {resultado_omitir_vocales}")
