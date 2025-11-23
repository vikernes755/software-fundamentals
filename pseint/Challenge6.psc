Algoritmo challenge_6
		
		Definir continuar Como Caracter
		Definir tiro, totalTiros, sumaTiros, pares, impares Como Entero
		
		totalTiros <- 0
		sumaTiros <- 0
		pares <- 0
		impares <- 0
		
		continuar <- "SI"
		
		Mientras continuar = "SI" Hacer
			
			tiro <- Aleatorio(1, 6)
			Escribir "Sacaste: ", tiro
			
			totalTiros <- totalTiros + 1
			sumaTiros <- sumaTiros + tiro
			
			Si tiro % 2 = 0 Entonces
				pares <- pares + 1
			SiNo
				impares <- impares + 1
			FinSi
			
			Escribir "¿Deseas lanzar de nuevo? (SI/NO): "
			Leer continuar
			continuar <- Mayusculas(continuar)
			
		FinMientras
		
		Escribir "-------------------------------"
		Escribir "Total de tiros efectuados: ", totalTiros
		Escribir "Suma total de los tiros: ", sumaTiros
		Escribir "Total de pares: ", pares
		Escribir "Total de impares: ", impares
	
	
FinAlgoritmo
