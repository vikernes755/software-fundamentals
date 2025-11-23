import os
from random import randint

live = 3
status = True

tiros = 0

def roll_dice():
    
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2

    

#print(roll_dice())

while True:
    key= input("Press any key to roll dices: ")
    
    tiros += 1
    
    dices = roll_dice()
    print(f"Dice1: {dices[0]}")
    print(f"Dice2: {dices[1]}")
    
    
    if (dices[0] + dices[1]) % 2 == 0:
        live +=1
        print(live)
    else:
        live -=1 
        print(live)
        
    if dices[0] == 6 and dices[1] == 6:
        print("You win")
        print(f"you won the roll: {tiros} 😊🎉")
        
        os.system("Pause")
        break
    if live == 0:
        print("Game over")
        print(f"you lost the roll: {tiros} 😢 ")
        break

