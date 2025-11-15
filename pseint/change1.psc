Algoritmo dados_par_o_impar
	definir dice1 Como Entero
	
	// dado
	dice1 <- Aleatorio(1,6)
	
	Escribir "Dado: ",dice1
	// determinar si es par o impar
	
	si dice1 % 2 = 0 Entonces
		Escribir "El número es par"
		
    SiNo
		escribir"El número es impar"
	FinSi

FinAlgoritmo