"""Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos."""

lista_alumnos = []


n = int(input("Ingrese la cantidad de alumnos: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")

    # Obtenemos las calificaciones del alumno
    calificaciones = []
    for j in range(3):
        nota = float(input(f"Ingrese la calificación {j + 1} para {nombre}: "))
        calificaciones.append(nota)

    # Creamos un diccionario con los datos del alumno
    alumno = {"Alumno": nombre, "Notas": calificaciones}
    lista_alumnos.append(alumno)

print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(f"{alumno['Alumno']}: {alumno['Notas']}")
