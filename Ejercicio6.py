"""Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores"""

def fibonacci_hasta_n(n):
    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Llamamos a la función con el valor 50
serie_fibonacci = fibonacci_hasta_n(50)


print("Serie de Fibonacci hasta 50:")
print(serie_fibonacci)

