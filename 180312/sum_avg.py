def Sum(s):
	result = 0

	for i in s:
		result += i
	
	return result

def Avg(s):
	sum = Sum(s)

	return sum / len(s)
