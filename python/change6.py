import random

def lanzar_dados():
    totalTiros = 0
    sumaTiros = 0
    pares = 0
    impares = 0

    continuar = "SI"

    while continuar == "SI":
        
        tiro = random.randint(1, 6)
        print("Sacaste:", tiro)

        totalTiros += 1
        sumaTiros += tiro

        if tiro % 2 == 0:
            pares += 1
        else:
            impares += 1

        continuar = input("¿Deseas lanzar de nuevo? (SI/NO): ").upper()

    print("-------------------------------")
    print("Total de tiros efectuados:", totalTiros)
    print("Suma total de los tiros:", sumaTiros)
    print("Total de pares:", pares)
    print("Total de impares:", impares)


# Llamar a la función para ejecutar el programa
lanzar_dados()