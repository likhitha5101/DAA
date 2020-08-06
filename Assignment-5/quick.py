def partition(arr,pivot):
	left = []
	right = []
	for i in arr:
		if i < pivot:
			left.append(i)
		elif i > pivot:
			right.append(i)
	index = len(left)
	left.extend([pivot])
	left.extend(right)
	
	return left,index

res_nuts = []
res_bolts = []

def solve(nuts,bolts):
	global res_nuts
	global res_bolts
	if len(nuts) == 0:
		return
	if len(nuts) == 1:
		res_nuts.extend(nuts)
		res_bolts.extend(bolts)
		return	

	pivot = nuts[ len(nuts) // 2 ]
	bolts,index  = partition(bolts,pivot)
	nuts,index = partition(nuts,bolts[index])
	solve(nuts[:index],bolts[:index])
	res_nuts.append(pivot)
	res_bolts.append(pivot)
	solve(nuts[index+1:],bolts[index+1:])

b=[5,2,1,4,9,8,6]
a=[1,4,6,8,9,5,2]
print("Order of Bolts: ",b)
print("Initial order of nuts: ",a)
solve(a,b)
print("Ordered bolts: ",res_bolts)
print("Ordered nuts: ",res_nuts)