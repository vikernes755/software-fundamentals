Algoritmo Reto_condicional4
	definir num1, num2, operation, result como real
	Escribir"Enter value to number 1: "
	leer num1
	Escribir"Enter value to number 2: "
	leer num2
	Escribir "select the operation you  want:"
	escribir "[1] addition"
	Escribir"[2] substration" 
	Escribir"[3] multiplication"
	Escribir "[4] Division"
	escribir"[5] All"
	leer operation
	si operation = 1 Entonces
		result = num1 + num2
		Escribir "Addition: " , result 
	FinSi
	si operation = 2 Entonces
		result = num1 - num2
		Escribir "Substraction: " , result 
	FinSi
	si operation = 3 Entonces
		result = num1 * num2
		Escribir "Multiplication: " , result 
	FinSi
	si operation = 4 Entonces
		si num2 > 0 Entonces
			result = num1 / num2
			Escribir "Division: " , result	
		SiNo
			Escribir "it is not possible to divide by zero"
		FinSi
		
	FinSi
	
	si operation = 5 Entonces
		result = num1 + num2
		Escribir "Addition: " , result
		
		result = num1 - num2
		Escribir "Substraction: " , result
		
		result = num1 * num2
		Escribir "Multiplication: " , result 
		
		si num2 > 0 Entonces
			result = num1 / num2
			Escribir "Division: " , result	
		SiNo
			Escribir "it is not possible to divide by zero"
		FinSi
		
	FinSi
	
	
FinAlgoritmo
