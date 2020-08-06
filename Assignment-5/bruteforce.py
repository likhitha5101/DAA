def matchnuts(nuts,bolts):
	n=len(nuts)
	for i in range(0,n):
		for j in range(0,n):
			if(nuts[j]==bolts[i]):
				nuts[i],nuts[j]=nuts[j],nuts[i]
	
	print("Arranged order of nuts: ",nuts)


bolts=[5,2,1,4,9,8,6]
nuts=[1,4,6,8,9,5,2]
print("Order of Bolts: ",bolts)
print("Initial order of nuts: ",nuts)
matchnuts(nuts,bolts)
