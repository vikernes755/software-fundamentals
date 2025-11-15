from random import randint

print ("cuantas veces quieres lanzar el dado")
lanzamiento = int(input())
suma = 0

for comntador in range(1, lanzamiento + 1):
    
    dado = randint(1,6)
    print(f"lanzamiento {comntador} : {dado}")
    
    suma = (suma + dado)
    
print(f"lasuma total es: {suma}")
