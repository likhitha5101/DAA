from Point import Point

n = int(input('Enter the number of ATMs: '))

l = []

print('Enter the coordinates of all the ATMs')
for i in range(n):
    x,y = tuple(map(float,input().split()))
    l.append(Point(x,y))

min1 = l[0]
min2 = l[1]

for i in range(n-1):
    for j in range(i+1,n):
        if l[i].distance(l[j]) < min1.distance(min2):
            min1 = l[i]
            min2 = l[j]

print('Remove Either among: ' + str(min1) + ' ' + str(min2) )
