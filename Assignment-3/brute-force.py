import time

def brute_force(arr):
	count=0
	n=len(arr)
	for i in range(n):
		for j in range(i+1,n):
			if(arr[i]>arr[j]):
				count+=1
	print(arr,"\tcount: ",count)

#def modify(arr):
	

s=time.time()

brute_force([4,5,2,1,3])

e=time.time()
print("time: ",e-s)