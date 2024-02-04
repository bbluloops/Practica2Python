"""En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
1636!
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
[
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]
"""

def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    # Eliminamos posibles espacios al principio y al final de la cadena
    fecha = fecha.strip()

    # Verificamos el formato de entrada es mes/día/año o Mes día, año
    if '/' in fecha:
        # Formato mes/día/año
        mes, dia, anio = map(int, fecha.split('/'))
    else:
        # Formato Mes día, año
        partes = fecha.split()
        mes = meses.index(partes[0]) + 1
        dia = int(partes[1].rstrip(','))
        anio = int(partes[2])

    # Generamos la fecha en formato AAAA-MM-DD
    fecha_convertida = f"{anio:04d}-{mes:02d}-{dia:02d}"
    
    return fecha_convertida

fecha_ingresada = input("Ingrese una fecha (en formato mes/día/año o Mes día, año): ")

fecha_convertida = convertir_fecha(fecha_ingresada)
print(f"Fecha en formato AAAA-MM-DD: {fecha_convertida}")
