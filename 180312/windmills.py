def draw():
	r = 10

	for i in range(0, r):
		for j in range(0, i + 1):
			print('*', end='')
		for j in range(0, r - (i + 1)):
			print(' ', end='')
		for j in range(0, r - i):
			print('*', end='')
		print()
	
	for i in range(0, r):
		for j in range(0, r - (i + 1)):
			print(' ', end='')
		for j in range(0, i + 1):
			print('*', end='')
		for j in range(0, i):
			print(' ', end='')
		for j in range(0, r - i):
			print('*', end='')
		print()
