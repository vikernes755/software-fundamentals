#Brayan Cortés de la Cruz
#Juan David Burbano Mejia 
#Angel Damian Bravo Enriquez
#Norvy Alejandra García Lara

from datetime import datetime

totalEmpleados = 0 
totalMasculino = 0
totalFemenino = 0
totalOtros = 0
sumaSalarios = 0
sumaEdades = 0 

continuar = "SI"

while continuar == "SI":
    nombres = input("Ingresar su nombre completo: ")

    # VALIDACIÓN EMAIL (DEBE CONTENER '@')
    while True:
        email = input("Ingresar tu correo electrónico: ")
        if "@" in email:
            break
        print("Error: El correo debe contener '@'.")

    # VALIDACIÓN CELULAR (SOLO NÚMEROS Y 10 DÍGITOS SIN isdigit)
    while True:
        celular = input("Ingresar tu número telefónico: ")
        es_num = True

        for c in celular:
            if c < "0" or c > "9":
                es_num = False

        if es_num and len(celular) == 10:
            break

        print("Error: El número debe tener 10 dígitos y solo números.")

    # Validación género
    while True:
        genero = input("Género (M/F/O): ").upper()
        if genero in ("M", "F", "O"):
            break
        else:
            print("El valor ingresado es inválido, debe ser (M/F/O).")

    salario = int(input("Ingresar salario: "))

    # VALIDACIÓN AÑO DE NACIMIENTO (4 DÍGITOS Y SER MAYOR DE 18)
    año_actual = datetime.now().year
    
    while True:
        añoDeNacimiento = input("Ingresa tu año de nacimiento (AAAA): ")

        # Validar que sean 4 dígitos numéricos
        if not (añoDeNacimiento.isdigit() and len(añoDeNacimiento) == 4):
            print(" Error: Debe ingresar SOLO un año de 4 dígitos (ej: 1999).")
            continue

        añoDeNacimiento = int(añoDeNacimiento)

        # Validar que no sea mayor al año actual
        if añoDeNacimiento > año_actual:
            print(f"Error: El año no puede ser mayor que {año_actual}.")
            continue
        
        # Validar edad mínima (18 años)
        edad = año_actual - añoDeNacimiento
        if edad < 18:
            print("Error: Debe ser mayor de 18 años para registrarse.")
            continue

        break  # Año válido

    totalEmpleados += 1

    if genero == "M":
        totalMasculino += 1
    elif genero == "F":
        totalFemenino += 1
    else:
        totalOtros += 1

    sumaSalarios += salario
    sumaEdades += edad

    # Continuar
    continuar = input("¿Desea agregar otro empleado? (SI/NO): ").upper()
    while continuar not in ("SI", "NO"):
        print("Solo SI o NO.")
        continuar = input("¿Desea agregar otro empleado? (SI/NO): ").upper()

# ------------ REPORTE FINAL ------------
print("Total empleados:", totalEmpleados)
print("Género M:", totalMasculino)
print("Género F:", totalFemenino)
print("Género O:", totalOtros)
print("Total salarios:", sumaSalarios)

if totalEmpleados > 0:
    print("Promedio edades:", sumaEdades / totalEmpleados)
else:
    print("Promedio edades: No aplica (sin empleados)")