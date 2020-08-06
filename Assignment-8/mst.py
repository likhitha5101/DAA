#!/usr/bin/env python
# coding: utf-8

# ## CS1403 — Design and Analysis of Algorithms
# 
# ### Session — 08

# ### Min Heap implementation

# In[1]:


class minheap(object):
    __slots__ = ['_size','_array']

    def __init__(self,firstOb):
        self._size = 0
        self._array = [firstOb]*1005
    
    def __len__(self):
        return self._size

    def display(self):
        i = 1
        while i <= self._size:
            print(str(self._array[i]))
            i = i + 1

    def insert(self,newOb):
        self._size = self._size + 1
        i = self._size
        
        while self._array[i//2] > newOb:
            self._array[i] = self._array[i//2]
            i = i // 2
    
        self._array[i] = newOb

    def delete(self):
        if self._size == 0:
            return None
        
        min = self._array[1]
        last = self._array[self._size]
        self._size = self._size - 1

        i = 1
        while i * 2 <= self._size:
            child = i * 2
        
            if child != self._size and self._array[child + 1] < self._array[child]:
                child += 1
            
            if last > self._array[child]:
                self._array[i] = self._array[child]
            else:
                break
            
            i = child

        self._array[i] = last
        return min


# ### Kruskal’s algorithm

# In[3]:


import numpy as np

class edge(object):
    __slots__ = ['_edge']

    def __init__(self,l=(-1,-1,-1)):
        self._edge = l

    def __lt__(self,other):
        return self._edge[2] < other._edge[2]

    def __gt__(self,other):    
        return self._edge[2] > other._edge[2]

    def getEdge(self):
        return self._edge

    def __str__(self):
        return str(self._edge)

class disjoint_set(object):
    __slots__ = ['_arr','_size']

    def __init__(self):
        self._arr = np.array([-1 for i in range(200)])
        self._size = 0

    def initialise(self,size):
        assert(type(size) == int and size <= 200)
        self._size = size - 1 

    def findClass(self,a):
        assert(type(a) == int)
        assert(a-1 <= self._size)

        a = a - 1
        while self._arr[a] > -1:
            a=self._arr[a]

        return a

    def merge(self,a,b):
        assert(type(a) == int and type(b) == int)
        assert(a-1 <= self._size and b-1 <= self._size)

        class_a = self.findClass(a)
        class_b = self.findClass(b)


        #Signs swapped since we are comparing negative numbers
        if self._arr[class_a] > self._arr[class_b]:
            self._arr[class_a] = class_b
        elif self._arr[class_a] < self._arr[class_b]:
            self._arr[class_b] = class_a
        else:
            self._arr[class_a] -= 1
            self._arr[class_b] = class_a

    def __str__(self):
        string = ''
        for x in range(self._size+1):
            string += ( str(self._arr[x]) + ' ' )
        return string

n = 100
e = 1000

with open('graph_ip.txt','r') as input_file:
    ip = input_file.read().split('\n')

    edges = []

    for i in range(e):
        edges.append(edge(tuple(map(int,ip[i].split(' ')))))


    heap = minheap(edge())

    for i in range(e):
        heap.insert(edges[i])

    ds = disjoint_set()
    ds.initialise(n)

    selected = []
    count = 0
    length = 0

    while len(heap):
        edgeTuple = heap.delete().getEdge()
        class_l = ds.findClass(edgeTuple[0])
        class_r = ds.findClass(edgeTuple[1])

        if class_l != class_r:
            selected.append(edgeTuple)
            ds.merge(edgeTuple[0],edgeTuple[1])
            count += 1
            length += edgeTuple[2]
            if count == n - 1:
                break

    print('The selected edges are: ',selected)
    print('Length of the path is : ',length)

