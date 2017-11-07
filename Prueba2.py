def funcion(numero):
	resultado = []
	resultado.insert(0, numero)
	for i in range(1,9):
		contador = 0
		nuevonumero = resultado[i-1]
		for nuevonumero in resultado:
			contador += 1
		resultado.insert(i, contador)

	return resultado



print(funcion(4))