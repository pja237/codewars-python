#!/usr/bin/python

def can_left(arr,x,y):
    return not (arr[x+1][y-1] or arr[x+1][y-2] or arr[x][y-1] or arr[x][y-2] or arr[x-1][y-1] or arr[x-1][y-2])

def can_right(arr,x,y):
    return not (arr[x+1][y+1] or arr[x+1][y+2] or arr[x][y+1] or arr[x][y+2] or arr[x-1][y+1] or arr[x-1][y+2])

def can_down(arr,x,y):
    return not (arr[x+1][y+1] or arr[x+2][y+1] or arr[x+1][y] or arr[x+2][y] or arr[x+1][y-1] or arr[x+2][y-1])

def can_up(arr,x,y):
    return not (arr[x-1][y+1] or arr[x-2][y+1] or arr[x-1][y] or arr[x-2][y] or arr[x-1][y-1] or arr[x-2][y-1])

def spiralize(size):
    ground=list()
    ground.append([1 for j in xrange(size+4)])
    for i in xrange(size+2): ground.append([1 if j==0 or j==size+3 else 0  for j in xrange(size+4)])
    ground.append([1 for j in xrange(size+4)])
    rez=spiral(ground,2,2,size+2)
    rez=rez[2:-2]
    rez=map(lambda i: i[2:-2],rez)
    return rez

def spiral(arr, x, y, n):
    if not arr[0]: return []

    can_go=True
    while can_go==True:

        arr[x][y]=1

        if not (x-1>=0 and arr[x-1][y]==0 and arr[x-2][y]==0) and can_right(arr,x,y):
            y=y+1
        elif can_down(arr,x,y):
            x=x+1
        elif can_left(arr,x,y):
            y=y-1
        elif can_up(arr,x,y):
            x=x-1
        else: can_go=False

    return arr


for i in spiralize(1):
    print i
print
for i in spiralize(2):
    print i
print
for i in spiralize(3):
    print i
print
for i in spiralize(4):
    print i
print
for i in spiralize(5):
    print i
print
for i in spiralize(10):
    print i

# snail([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]): 
# result: [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 17, 18, 19, 14, 13, 12, 11, 6, 7, 8, 9] 
# expect: [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
#print snail([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
#print snail(array_2)
#print snail(array_3)
#print snail(array_4)
#print snail(array) 
#print "#=> [1,2,3,4,5,6,7,8,9]"
#print snail(array_1) 
#print "#=> [1,2,3,6,9,8,7,4,5]"
