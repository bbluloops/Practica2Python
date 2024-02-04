"""Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
n = 5 
# Imprimimos la mitad superior
for i in range(n):
    print("* "*(i+1))

# Imprimir la mitad inferior
for i in range(n - 2,-1,-1):
    print("* " * (i + 1))

