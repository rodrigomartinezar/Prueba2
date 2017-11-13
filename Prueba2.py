import itertools

def lookandsay(numero):
	return "".join(str(sum(1 for x in g)) + k for k,g in itertools.groupby(numero))

	
def funcion(num):
	seq = [num]
	for x in range(9):
		seq.append(lookandsay(seq[-1]))
	return seq


print(funcion('1'))