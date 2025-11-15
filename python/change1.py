from random import randint

dado =  randint(1,6)

print(f"dado es: {dado}")

if dado % 2 == 0: 
    print ("El número es par")
else: 
    print("El número es impar")

