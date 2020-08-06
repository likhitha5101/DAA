#THIS IN AN INCOMPLETE VERSION
''' 
Idea for optimizing the brute force approach for
finding no. of out-of-order-pairs: 

* with the help of merge sort find the no. of swappings that occur
during the merging of sublists. The sum of all swapings will give us 
no. of out-of-order pairs.

* the complexity of brute force version is O(n^2)

* the complexity of merge sort approach is O(nlogn)
'''

def mergeSort(arr,count): 
    if len(arr) >1: 
        mid = len(arr)//2  
        L = arr[:mid]   
        R = arr[mid:]  
  
        count = mergeSort(L,count) # Sorting the first half 
        count = mergeSort(R,count) # Sorting the second half 
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
                count+=1
            else: 
                arr[k] = R[j] 
                j+=1
                count+=1
            k+=1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
            count+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
            count+=1
    return count

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 

count=0
arr = [4,5,2,1,3]  
print ("Given array is", end="\n")  
printList(arr) 
count = mergeSort(arr,count) 
print("Sorted array is: ", end="\n") 
printList(arr) 
print(count)