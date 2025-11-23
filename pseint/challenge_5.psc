Algoritmo challenge_5
	Definir dado1, contador, lanzamiento, pares, impares Como Entero
	
	escribir "cuantas veces quieres lanzar los dados:"
	leer lanzamiento
	pares = 0
	impares = 0
	
	
	contador = 0
	Para contador = 1 hasta lanzamiento con paso 1
		
		dado1 = Aleatorio(1,6)
		
		Escribir "Lanzamiento ", contador , ": ", dado1
		
		si dado1 % 2 = 0 Entonces
			pares = pares + 1
			
		SiNo
			impares = impares + 1
			
		FinSi
		
		
		
	FinPara
	
	escribir "pares: ", pares
	escribir "impares: ", impares
	
	
	
FinAlgoritmo
