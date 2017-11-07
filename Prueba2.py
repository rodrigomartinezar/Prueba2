def funcion(numero):
	resultado = []
	resultado.append(numero)   ##transformar a Strings los numeros
	#resultado.append(numero)
	nuevonumero = numero
	for i in range(1,9):
		largo = len(resultado)
		contador = 0
		prev = resultado [i-1]
		if nuevonumero == prev:
			contador += 1
		resultado.append(contador)
		resultado.append(nuevonumero)
		nuevonumero = contador
	return resultado



print(funcion(5))