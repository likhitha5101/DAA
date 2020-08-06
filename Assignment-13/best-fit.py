#!/usr/bin/env python
# coding: utf-8

# ## CS1403 — Design and Analysis of Algorithms
# ### Session — 13

# 1. Consider the n-puzzle, where we have tiles numbered from 1 . . . (n2 − 1) placed in a grid of n × n. Following is an instance of 3-puzzle where tiles numbered 1 . . . 8 are placed on a 3 × 3 grid.
# 

# In[1]:


import numpy as np
import heapq as heap
import copy


# In[2]:


class stateClass(object):
    __slots__ = ['_state','n','actual_position','depth','a_star']
    
    def __init__(self,state=None,n=None,depth=None,a_star=False):
        self.actual_position = {}
        self._state = state
        self.n = n
        self.depth = depth
        self.a_star = a_star
        for i in range(1, (n ** 2)):
            self.actual_position[i] = (((i - 1)// n) , ((i - 1) % n))
    
    def heuristics(self):
        count = 0
        
        if self.a_star:
            count = self.depth
        
        sequence = self._state
        for i in range(self.n):
            for j in range(self.n):
                if sequence[i][j] != 0:
                    actual_loc = self.actual_position[sequence[i][j]]
                    count = count +  (abs(actual_loc[0] - i)  + abs(actual_loc[1] - j))
        
        return count
    
  

    def generate_states(self):
        sequence = self._state
        space_i = -1
        space_j = -1

        for i in range(self.n):
            for j in range(self.n):
                if sequence[i][j] == 0:
                    space_i = i
                    space_j = j

        for row_add,col_add in [(-1,0),(1,0),(0,1),(0,-1)]:
                temp_sequence = copy.deepcopy(sequence)
                if space_i + row_add >= 0 and space_i + row_add < self.n                   and space_j + col_add >= 0 and space_j + col_add < self.n:
                    temp_sequence[space_i][space_j],temp_sequence[space_i + row_add][space_j + col_add]=                    temp_sequence[space_i + row_add][space_j + col_add],temp_sequence[space_i][space_j]

                    yield stateClass(temp_sequence,self.n,self.depth + 1,self.a_star)


    def __str__(self):
        return '\nState:\n' + str(self._state) + '\nDepth: ' + str(self.depth)

    def __lt__(self,other):
        return self.heuristics() < other.heuristics()
    
    def __gt__(self,other):
        return self.heuristics() > other.heuristics()
    
    def __eq__(self,other):
        for i in range(self.n):
            for j in range(self.n):
                if self._state[i][j] != other._state[i][j]:
                    return False
        return True


# In[3]:


N = int(input())

l = []

for i in range(N):
    l.append(list(map(int,input().split(' '))))

    
input_array = np.array(l)


# The following function works for both A-Star and other heuristics function
# 
# Argument	
# Input_array	-input state which is to be solved,
# 
# Shape -	shape of the array  $n^{2}$,
# 
# Mode -	$A^{*}$ mode or normal

# In[5]:


def solve_best_first(input_array,shape,Mode=''):
    try:
        assert(type(Mode) == str)
        if Mode != 'A-Star' and Mode != 'H1':
            print(Mode)
            raise AssertionError()
    except AssertionError:
        print('Please Enter a valid String for Mode[A-Star,H1]')
        return
    
    def isGoalState(state):
        for i in range(N):
            for j in range(N):
                if state[i][j] != (i * 3 + (j + 1)) % 9:
                    return False
        return True

    
    if Mode == 'A-Star':
        print('Using A* Heuristics!\n')
        input_state = stateClass(state = input_array, n = N, depth = 0, a_star=True)
    else:
        print('Using H1 Heuristics!\n')
        input_state = stateClass(state = input_array, n = N, depth = 0, a_star=False)
        
    state_list = [input_state]
    visited_states = []
    solution_seq = []
    
    
    def best_first_recursion(state):
        possibilities = []
        
        if isGoalState(state._state):
            print('\nSolution Reached in: %d steps' % (state.depth))
            return True
        
        if state in visited_states:
            return False
        
        visited_states.append(state)
        
        for successor in state.generate_states():
            if successor not in visited_states:
                heap.heappush(possibilities,successor)
            
        while len(possibilities):
            next_state = heap.heappop(possibilities)
            if best_first_recursion(next_state):
                solution_seq.insert(0,next_state)
                return True
        return False
    
    best_first_recursion(input_state)
    solution_seq.insert(0,input_state)
    for steps in solution_seq:
        print(steps)


# In[6]:


solve_best_first(input_array,N,'A-Star')


# In[7]:


solve_best_first(input_array,N,'H1')

