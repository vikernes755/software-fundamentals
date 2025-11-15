gitAlgoritmo contar_dados
	definir lanzamiento, contador, dado Como Entero
	definir lan1 , lan2 , lan3 , lan4, lan5 , lan6 Como Entero
	lan1 = 0
	lan2 = 0
	lan3 = 0
	lan4 = 0
	lan5 = 0
	lan6 = 0
	
	escribir "ingresael numero de veces que quieres lanzar el dado"
	leer lanzamiento
	
	para contador = 1 hasta lanzamiento Hacer
		dado = Aleatorio(1,6)
		
		si dado = 1 Entonces
			lan1 = lan1 + 1
			
		FinSi
		si dado = 2 Entonces
			lan2 = lan3 + 1
		FinSi
		
		si dado = 3 Entonces
			lan3 = lan3 + 1
			
		FinSi
		si dado = 4 Entonces
			lan4 = lan4 + 1
			
		FinSi
		
		si dado = 5 Entonces
			
			lan5= lan5 +1
			
		FinSi
		si dado = 6 entonces
			lan6 = lan6 +1
			
		FinSi
	FinPara
	escribir "resultados"
	escribir "1 salio: ", lan1, " veces"
	Escribir "salio: ", lan2, " veces"
	escribir "3 salio: " , lan3, " veces"
	escribir "4salio: ", lan4, "veces"
	escribir "5 salio: " lan5, "veces"
	escribir "6 salio: " lan6, " veces"
	
	
FinAlgoritmo
