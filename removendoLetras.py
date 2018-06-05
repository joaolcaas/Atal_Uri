def backtracking(entrada):
	if(len(entrada) <= 2):
		return
	for i in range(len(entrada)):
		new = entrada[:i] + entrada[i+1:]
		if(new not in set_datas):
			set_datas.add(new)
			backtracking(new)


while True:
	try:
		global set_datas
		set_datas = set()
		entrada = input()
		set_datas.add(entrada)
		
		for i in range(len(entrada)):
			set_datas.add(entrada[i])
			
		backtracking(entrada)
		final_list = list(set_datas)
		final_list.sort()
		for i in final_list:
			print(i)
		print()
	except EOFError:
		break
			
			
