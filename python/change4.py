from random import randint

lanzamiento = int(input("¿Cuántas veces quieres lanzar los dados? "))

contador = 0


while True:
    contador += 1
    
    dado1 = randint(1,6)
    dado2 = randint (1,6)
    
    print(F"Lanzamiento {contador} : {dado1} y {dado2}")
    
    if (dado1 == 6 and dado2 == 6) or (contador == lanzamiento):
        break
    
if dado1 == 6 and dado2 == 6:
    print(f"¡Salió par de SEIS en el lanzamiento {contador}!")
else:
    print(f"Se completaron los {lanzamiento} lanzamientos sin obtener par de seis.")