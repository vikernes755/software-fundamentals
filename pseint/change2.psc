Algoritmo LanzarDadoVariasVeces
	Definir lanzamiento, suma, dado,  contador Como Entero
	
	Escribir "Cuantas veces quieres lanzar el dado"
	leer lanzamiento
	
	suma =  0
	para contador = 1 hasta lanzamiento Hacer
		dado = Aleatorio(1,6)
		Escribir "lanzamiento ", contador, ": ", dado
		
		suma = suma + dado
		
	FinPara
	
	escribir "lasuma total es: " , suma
	
FinAlgoritmo
