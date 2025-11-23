from random import randint

lanzamiento = int(input("¿Cuántas veces quieres lanzar los dados? "))

contador = 0
pares = 0
impares = 0


for contador in range (1, lanzamiento + 1 ):
    
    dado = randint(1,6)    
    
    if (dado % 2 == 0):
        
        pares += 1
        
    else:
        impares += 1
        
        
print("resultados")  

print(f"pares: {pares}")
print(f"impares: {impares}")
          
        
    
    
    
    
    
    