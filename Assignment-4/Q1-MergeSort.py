import random
import time
import math

from Point import Point
from Queue import LinkedQueue


def solve(q,refPoint,toPrint=True):
    assert type(toPrint) == bool
    
    def merge(q1,q2):
        nonlocal refPoint
        res = LinkedQueue()

        while q1.isEmpty() == False and q2.isEmpty() == False:
            if q1.front().distance(refPoint) < q2.front().distance(refPoint):
                res.enqueue(q1.dequeue())
            else:
                res.enqueue(q2.dequeue())
        while q1.isEmpty() == False:
            res.enqueue(q1.dequeue())
        while q2.isEmpty() == False:
            res.enqueue(q2.dequeue())
            
        return res

    def mergeSort(q):
        if len(q) == 1:
            return q
        
        size = len(q)
        half = size//2

        left_q = LinkedQueue()
        right_q  = LinkedQueue()

        for i in range(0,half):
            left_q.enqueue(q.dequeue())
        for i in range(half,size):
            right_q.enqueue(q.dequeue())
        
        left_q = mergeSort(left_q)
        right_q = mergeSort(right_q)

        return merge(left_q,right_q)

    result_q = mergeSort(q)

    while result_q.isEmpty() == False and toPrint:
        print(str(result_q.dequeue()))

print("To Check Algorith Correctness: ")
n = 0
q = LinkedQueue()
print('Enter the number of points: ')
n = int(input())
print('Enter the points[x,y]: ')

for i in range(n):
    x,y = tuple(map(float,input().split()))
    q.enqueue(Point(x,y))

print('Enter the referance point[x,y]: ')
x,y = tuple(map(float,input().split()))
refPoint = Point(x,y)

solve(q,refPoint)


print("\nFinding Time Complexity: \n\n")

print("+-----------+----------------+--------------------+----------------+----------------+")
print("|   Size    |       N        |         N^2        |     N Log N    |   Time Taken   |")
print("+-----------+----------------+--------------------+----------------+----------------+")

length = random.randint(29000,30000)


for iter in range(15):
    q = LinkedQueue()
    for size in range(length):
        q.enqueue(Point(random.randint(-100,100),random.randint(-200,350)))
    
    #Queue with values is now ready
    start = time.time()
    
    solve(q,refPoint,False)
    
    end = time.time()
    timeTaken = (end-start)

    print("| %9d | %14.12f | %18.16f | %14.12f | %14.12f |" % (length,(timeTaken /length),(timeTaken/(length**2)),(timeTaken/(length * math.log(length))),timeTaken))
    length += 2000

print("+-----------+----------------+--------------------+----------------+----------------+")
