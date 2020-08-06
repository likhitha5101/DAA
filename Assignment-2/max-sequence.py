import time
import random
import math
import csv

def findmax(arr):
	maxsum=0
	n=len(arr)
	for i in range(0,n):
		for j in range(i,n):
			thissum=0
			for k in range(i,j+1):
				thissum+=arr[k]
			if(thissum > maxsum):
				maxsum=thissum
	return maxsum

def dynamicprog(arr):
	maxsum=0
	n=len(arr)
	for i in range(0,n):
		thissum=0
		for j in range(i,n):
			thissum+=arr[j]
			if(thissum > maxsum):
				maxsum=thissum
	return maxsum

def version3(arr):
	maxsum=thissum=0;
	n=len(arr)
	for j in range(n):
		thissum+=arr[j]
		if(thissum>maxsum):
			maxsum=thissum
		elif(thissum < 0):
			thissum = 0
	return maxsum

analysis1=[]
analysis2=[]
analysis3=[]

for n in range(10,101,10):
	arr=random.sample(range(-100,100),n)
	m=10
	sum1=sum2=sum3=0
	for i in range(m):
		start = time.process_time()
		findmax(arr)
		end = time.process_time()
		sum1+=end-start
	avg1=sum1/m
	
	for i in range(m):
		start = time.process_time()
		dynamicprog(arr)
		end = time.process_time()
		sum2+=end-start
	avg2=sum2/m

	for i in range(m):
		start = time.process_time()
		version3(arr)
		end = time.process_time()
		sum3+=end-start
	avg3=sum3/m
	
	analysis1+=[[n,avg1,math.log(n,10),(avg1/math.log(n,10)),n,avg1/n,n**2,avg1/n**2,n**3,avg1/n**3,2**n,avg1/2**n]]
	analysis2+=[[n,avg2,math.log(n,10),(avg2/math.log(n,10)),n,avg2/n,n**2,avg2/n**2,n**3,avg2/n**3,2**n,avg2/2**n]]
	analysis3+=[[n,avg3,math.log(n,10),(avg3/math.log(n,10)),n,avg3/n,n**2,avg3/n**2,n**3,avg3/n**3,2**n,avg3/2**n]]

with open("brute-force.csv", "w",newline="") as f1:
    writer = csv.writer(f1)
    writer.writerow(["n","T(n)","log(n,10)","T(n)/math.log(n,10)","n","T(n)/n","n**2","T(n)/n**2","n**3","T(n)/n**3","2**n","T(n)/2**n"])
    writer.writerows(analysis1)
    
with open("dynamic-prog.csv", "w",newline="") as f2:
    writer = csv.writer(f2)
    writer.writerow(["n","T(n)","log(n,10)","T(n)/math.log(n,10)","n","T(n)/n","n**2","T(n)/n**2","n**3","T(n)/n**3","2**n","T(n)/2**n"])
    writer.writerows(analysis2)
    
with open("greedy.csv", "w",newline="") as f3:
    writer = csv.writer(f3)
    writer.writerow(["n","T(n)","log(n,10)","T(n)/math.log(n,10)","n","T(n)/n","n**2","T(n)/n**2","n**3","T(n)/n**3","2**n","T(n)/2**n"])
    writer.writerows(analysis3)