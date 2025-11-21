Algoritmo Lanzar_dados_hasta_que_sea_par_de_seis
	
	definir lanzamiento, contador, dado1, dado2 Como Entero
	escribir "cuantas veces quieres lanzar los dados:"
	leer lanzamiento
	
	contador = 0
	Repetir
		
		contador = contador + 1
		dado1 = Aleatorio(1,6)
		dado2 = aleatorio (1,6)
		
		escribir "lanzamiento", contador, ":" , dado1, "y", dado2
		
		
		
	Hasta Que (dado1 = 6 y dado2 = 6) o (contador = lanzamiento)
	
	Si (dado1 = 6 Y dado2 = 6) Entonces
        Escribir "¡Salió par de SEIS en el lanzamiento ", contador, "!"
    SiNo
        Escribir "Se completaron los ", lanzamiento, " lanzamientos sin obtener par de seis."
    FinSi
	
	
FinAlgoritmo
