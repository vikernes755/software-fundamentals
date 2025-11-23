status = True
acum = pares = impares = negativos = positivo =  positivosp = negativosp = positivosim = negativosim = suma = 0

while status:
    num = int(input("Press any number (0 to exit): "))

    if num == 0:      
        break   
    suma += num
    acum += 1

    # PAR / IMPAR
    if num % 2 == 0:
        pares += 1
        if num > 0:
            positivosp += 1
        else:
            negativosp += 1
    else:
        impares += 1
        if num > 0:
            positivosim += 1
        else:
            negativosim += 1

    # POSITIVOS / NEGATIVOS
    if num > 0:
        positivo += 1
    else:
        negativos += 1


print(f"pares {pares}")
print(f"impares {impares}")
print(f"la suma es {suma}")  
print(f"Positivos: {positivo}")
print(f"Negativos: {negativos}")
print(f"Total de números ingresados: {acum}")
print(f"Positivos pares: {positivosp}")
print(f"Negativos pares: {negativosp}")
print(f"Positivos impares: {positivosim}")
print(f"Negativos impares: {negativosim}")
