def median( list ):
	b = list[:]
	b.sort()
	return b[len(b)//2]
