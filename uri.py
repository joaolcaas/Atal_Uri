

while True:
	try:
		a,b = map(int,input().split())
		set_of_datas = set()

		if(a == 1):
			qq = input()
			print('Lucky Denis!')
		elif(a == 2):
			weight_1,weight_2 = map(int,input().split())
			for i in range(b):
				for k in range(b):
					total = (i + 1) * weight_1 + (k + 1) * weight_2
					set_of_datas.add(total)
					
			if(len(set_of_datas) == b**a ):
				print('Lucky Denis!')
			else:
				print('Try again later, Denis...')
		else:
			weight_1,weight_2,weight_3 = map(int,input().split())
			for i in range(b):
				for k in range(b):
					for j in range(b):
						total = (i + 1) * weight_1 + (k + 1) * weight_2 + (j + 1) * weight_3
						set_of_datas.add(total)
			if(len(set_of_datas) == b ** a):
				print('Lucky Denis!')
			else:
				print('Try again later, Denis...')
	except EOFError:
		break
			
			
