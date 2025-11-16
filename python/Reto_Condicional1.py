from random import randint  

dado1 = randint(1,6)
dado2 = randint(1,6)

print(f"Dace 1: {dado1} - Dace 2: {dado2}")
if dado1 == dado2:
    print("YOU WIN")
else:
    print("GAME OVER")
if dado1 % 2 == 0:
    print("Dace 1: PAR")
else:
    print("Dace 1: IMPAR")
if dado2 % 2 == 0:
    print("Dace 2: PAR")
else:
    print("Dace 2: IMPAR")
