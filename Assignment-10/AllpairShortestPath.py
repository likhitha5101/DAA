#!/usr/bin/env python
# coding: utf-8

# ## CS1403 — Design and Analysis of Algorithms
# Session — 10

# Problem 1: Given a directed graph G = (V, E), find the reachability between any two pair of vertices.

# In[2]:


import numpy as np

v = int(input())
e = int(input())

adjacency = np.array([[False for j in range(v)] for i in range(v)])

for edge in range(e):
    ip = tuple(map(int,input().split(' ')))
    adjacency[ip[0] - 1][ip[1] - 1] = True

for k in range(v):
    for i in range(v):
        for j in range(v):
            adjacency[i][j] = (adjacency[i][j]) or (adjacency[i][k] and adjacency[k][j])

print(adjacency)


# Problem 2: Given a weighted directed graph G = (V, E), find shortest weighted paths between every pair of nodes.

# In[3]:


import math
import numpy as np

v = int(input())
e = int(input())

distance = np.array([[math.inf for j in range(v)] for i in range(v)])
previous = np.array([[None for j in range(v)] for i in range(v)])

for edge in range(e):
    ip = tuple(map(int,input().split(' ')))
    distance[ip[0] - 1][ip[1] - 1] = ip[2]
    previous[ip[0] - 1][ip[1] - 1] = ip[0] - 1

for k in range(v):
    for i in range(v):
        for j in range(v):
            if distance[i][j] > (distance[i][k] + distance[k][j]):
                distance[i][j] = distance[i][k] + distance[k][j]
                previous[i][j] = k

print('The Distance Matrix Is:\n')
print(distance)

print('\n\nThe Previous Matrix Is: \n')
print(previous)


def path_display(source,dest,distance=0):
    global previous

    if dest == source:
        return str(source+1)

    if previous[source][dest] is None:
        return 'No path from %d to %d' % (source + 1,dest + 1)
    
    return path_display(source,previous[source][dest]) + ' --> ' + str(dest + 1)

print('\nThe paths are:')

for i in range(v):
    for j in range(v):
        print(path_display(i,j))
    print('-------------------------------')


# In[ ]:




