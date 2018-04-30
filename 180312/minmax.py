def Min(arr):
	min = arr[0]
	for i in arr:
		if min > i:
			min = i

	return min

def Max(arr):
	max = arr[0]

	for i in arr:
		if max < i :
			max = i

	return max
