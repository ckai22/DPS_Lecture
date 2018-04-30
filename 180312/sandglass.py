
def drawSandglass():
	r = int(input('row: '))

	for i in range(0, r):
		for j in range(0, i + 1):
			print(' ', end="")
		for j in range(0, 2 * (r - i) - 1):
			print('*', end="")
		print()

	for i in range(0, r):
		for j in range(0, r - i):
			print(' ', end="")
		for j in range(0, 2 * i + 1):
			print('*', end="")
		print()
