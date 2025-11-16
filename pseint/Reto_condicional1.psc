Algoritmo Reto_condicional_1
	definir dado1, dado2 Como Entero 
	
	dado1 = Aleatorio(1,6);
	dado2 = Aleatorio(1,6);
	
	Escribir "Dace 1: ", dado1, " Dace 2: ", dado2;
	si (dado1 = dado2) Entonces
		escribir"YOU WIN";
	SiNo
		escribir "GAME OVER";
	FinSi
	
	si (dado1 % 2 = 0 ) Entonces
		escribir "PAR"
	SiNo
		escribir"IMPAR"
	FinSi
	
	si (dado2 % 2 = 0) Entonces
		escribir "PAR"
	SiNo
		escribir"IMPAR"
	FinSi
	
	
FinAlgoritmo
