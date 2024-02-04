"""Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
Ejemplo:
“Desea ingresar un número?”: SI
“Ingrese el número:” 5
“¿Desea ingresar un número?”: SI
“Ingrese el número: ” 7
……
“Desea ingresar un número?”: NO
"""
numeros =[]
nump=0
numi=0

while True:
    ingreso=(input("¿Desea ingresar un número?(SI/NO): ")).upper()
    if ingreso=="SI":
        num=int(input("Ingrese el número: "))
        numeros.append(num)
        if num%2==0:
            nump+=1
        else:
            numi+=1
    elif ingreso=="NO":
            break
    else:
        print("Respuesta no válida. Por favor, ingrese 'SI' o 'NO'.")

print(f"Numeros ingresados: {numeros}")
print(f"Cantidad de numeros pares: {nump}")
print(f"Cantidad de numeros impares: {numi}")


       
