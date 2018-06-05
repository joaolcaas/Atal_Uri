

def policia_ou_ladrao(x,y,matrix,way):
	if(can_walk(x,y,matrix,way)):
		way[x][y] = 1
		policia_ou_ladrao(x - 1,y,matrix,way)
		policia_ou_ladrao(x + 1,y,matrix,way)
		policia_ou_ladrao(x,y - 1,matrix,way)
		policia_ou_ladrao(x,y + 1,matrix,way)
	else:
		return False

def can_walk(x,y,matrix,caminho):
	if(x >= 0 and y >= 0 and x <5 and y <5):
		if(matrix[x][y] == 0 and caminho[x][y] == 0):
			return True
		else:
			return False
	else:
		return False	
	
def create__all_zero():
	zero = []
	for i in range(5):
		aux = []
		for l in range(5):
			aux.append(0)
		zero.append(aux)
	return zero
			

num_matrizes = int(input())
contador = 0
 



while(contador < num_matrizes):
	matrix = []
	line = input()
	if(len(line.strip()) > 0):
		contador +=1
		matrix.append(list(map(int, line.split())))
		for i in range(4):
			line = input()
			matrix.append(list(map(int, line.split())))
	
		
		caminho = create__all_zero()
		

		status = policia_ou_ladrao(0,0,matrix,caminho)
	
		if(caminho[4][4] == 1):
			print('COPS')
		else:
			print('ROBBERS')
