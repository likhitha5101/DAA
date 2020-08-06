#heap implementation for a general list structure

def insert(h,x):
    h1=h+[0]
    size=len(h)+1
    i=size-1
    while(h1[i//2]>x and i>0):
        h1[i]=h1[i//2]
        i=i//2
    h1[i]=x
    return h1

def buildHeap(lst):
    h=[-999]
    for x in lst:
        h=insert(h,x)
    return h

def deleteMin(h):
    if(len(h)==1):
        print("Heap is empty...")
        return
    size=len(h)-1
    min=h[1]
    last=h[size]
    i=1
    while(i*2<=size):

        child=i*2
        if(child!=size and h[child+1]<h[child]):
            child=child+1
        if(last > h[child]):
            h[i]=h[child]
        else:
            break;

        i=child

    h[i]=last
    h=h[:-1]
    return h,min

a=[10,5,20,3,7,1]
h=buildHeap(a)
print("Array: ",a,"\nAfter buildheap():",h[1:])
h=insert(h,2)
print("After inserting 2 : ",h[1:])
h,m=deleteMin(h)
print("After deleting min :" ,h[1:],"\nMin element: ",m)

p=[0.24,0.16,0.11,0.09,0.40]
h=buildHeap(p)[1:]
print(h)