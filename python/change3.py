

from random import randint
lan1 = 0
lan2 = 0
lan3 = 0
lan4 = 0
lan5 = 0
lan6 = 0


print("ingresa el número de veces que quieres lanzar")
lanzamiento = int(input())


for contador in range (1, lanzamiento + 1 ):
    
    dado = randint(1,6)    
    
    if (dado == 1):
        
        lan1 = lan1 + 1
        
    elif (dado == 2):
        lan2 = lan2 + 1
        
    elif (dado == 3):
        lan3 = lan3 + 1
    
    elif (dado == 4):
        
        lan4 = lan4 + 1
        
    elif (dado == 5):
        lan5 = lan5 + 1
        
    else:
        lan6 = lan6 + 1    
print ("Resultados:")
    
print(f"1 salio: {lan1} veces")
print(f"2 salio: {lan2} veces")
print(f"3 salio: {lan3} veces")
print(f"4 salio: {lan4} veces")
print(f"5 salio: {lan5} veces")
print(f"6 salio: {lan6} veces")


        
        
    