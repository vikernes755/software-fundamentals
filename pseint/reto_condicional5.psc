Algoritmo reto_condicional5
	definir salariofinal Como Entero
	
	Escribir "Tipo de identificación (CC, PS, CE, CI): "
    Leer tipo_id
	
    Escribir "Nombres: "
    Leer nombres
	
    Escribir "Apellidos: "
    Leer apellidos
	
    Escribir "Genero (M/F): "
    Leer genero
	
    Escribir "Año de nacimiento: "
    Leer anio_nacimiento
	
    Escribir "Dirección: "
    Leer direccion
	
    Escribir "Teléfono: "
    Leer telefono
	
    Escribir "Salario: "
    Leer salario
	
    Si salario <= 1200000 Entonces
        Si genero = "F" O genero = "f" Entonces
            aumento <- salario * 0.10
        SiNo
            aumento <- salario * 0.08
        FinSi
		
    Sino
        Si salario < 2000000 Entonces
            aumento <- salario * 0.05
        Sino
            Si genero = "F" O genero = "f" Entonces
                aumento <- salario * 0.03
            SiNo
                aumento <- salario * 0.025
            FinSi
        FinSi
    FinSi
	
    salariofinal <- salario + aumento
	
    Escribir ""
    Escribir "------ RESULTADOS ------"
    Escribir "Nombre: ", nombres, " ", apellidos
    Escribir "Salario inicial: ", salario
    Escribir "Aumento aplicado: ", aumento
    Escribir "Salario final: ", salariofinal
	
FinAlgoritmo