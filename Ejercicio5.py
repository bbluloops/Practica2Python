"""Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4
Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
count.
"""

def cant_digitos(num, digito):
    #convertire el num en cadena para usar el metodo count
    str_num=str(num)
    cant=str_num.count(str(digito))

    print(f"Cantidad de veces {digito} en el numero {num} es: {cant}")

num_ingresado=int(input("Ingrese un numero entero: "))
digito_ingresado=int(input("Ingrese un digito: "))

cant_digitos(num_ingresado,digito_ingresado)