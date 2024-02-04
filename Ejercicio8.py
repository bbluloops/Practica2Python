"""Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.
"""
def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos"
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero_ingresado = int(input("Ingrese un número no negativo para calcular su factorial: "))

resultado_factorial = factorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es: {resultado_factorial}")
