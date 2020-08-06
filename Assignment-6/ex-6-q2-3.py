class node:
    def __init__(self,prob,sym,left,right):
        self.prob=prob
        self.sym=sym
        self.left=left
        self.right=right
        self.bs=""

def insert_c(h,x):
    h1=h+[node(0,'','','')]
    size=len(h)+1
    i=size-1
    while(h1[i//2].prob>x.prob and i>0):
        h1[i]=h1[i//2]
        i=i//2
    h1[i]=x
    return h1

def buildHeap_c(lst):
    h=[node(-999,'','','')]
    for x in lst:
        h=insert_c(h,x)
    return h

def deleteMin_c(h):
    if(len(h)==1):
        print("Heap is empty...")
        return
    size=len(h)-1
    min=h[1]
    last=h[size]
    i=1
    while(i*2<=size):

        child=i*2
        if(child!=size and h[child+1].prob<h[child].prob):
            child=child+1
        if(last.prob > h[child].prob):
            h[i]=h[child]
        else:
            break;

        i=child

    h[i]=last
    h=h[:-1]
    return h,min


def tree_implement(lst,sym):
    tree_list=[]
    
    for i in range(len(lst)):
        tree_list+=[node(lst[i],sym[i],'none','none')]
    
    return tree_list

def traverse(heap,bs):
    if(heap!='none'):
        traverse(heap.left,'0'+bs)
        if(heap.left=='none'and heap.right=='none'):
            heap.bs=bs[::-1]
        traverse(heap.right,'1'+bs)

p=[0.24,0.16,0.11,0.09,0.40]
sym=['a','b','c','d','e']
tree_list=tree_implement(p,sym)

heap=buildHeap_c(tree_list)

while(len(heap)!=2):
    heap,left=deleteMin_c(heap)
    heap,right=deleteMin_c(heap)

    prob=left.prob+right.prob
    left.bs='0'+left.bs
    right.bs='1'+right.bs
        
    res=node(prob,'',left,right)
    heap=insert_c(heap,res)

traverse(heap[1],'')

avg=0
print("Symbol\tProbability\tBinary code\n")
for i in tree_list:
    print(i.sym,"\t",i.prob,"\t\t",i.bs)
    avg+=i.prob*len(i.bs)
print("\nAverage Symbol length: %.2f"%avg)