import os 
status = True

acum, pares,  impares,  negativos,  positivo, positivosp, negativosp, positivosim, negativosim, suma = 0

 #while status == true
 #while true:
 
while status:
    num = int(input("Press any number (0 to exit)"))
    
    sum += num
    
    if num != 0:
        
        acum = acum +1
        if (num % 2 ==0):
            pares += 1
        else:
            impares += 1 
            
            
            
        if (num > 0):
           positivo += 1
           
        else:
            negativos += 1
            
            
            
        if (num % 2 == 0) and (num > 0):
            
            positivosp += 1
            
        elif(num % 2 == 0) and (num < 0):
            
            negativosp = negativosp +1
        elif (num % 2 != 0) and (num < 0):
            
            positivosim += 1
        else:
            
            negativosim += 1
    
    
    if num == 0:
        status = False
        break
    
        



print(f"pares {pares}")
print(f"impares {impares}")
print(f"la suma es {sum}")  
print(f"Positivos: {positivo}")
print(f"negativos: {negativos}")
print (F"total de numeros ingresados {acum}")
print(f"positivos pares {positivosp}")
print(f"negativo pares {negativosp}")
print(f"positivos impares {positivosim}")
print(f"negativo impares {negativosim}")





  
    
        
        
    
