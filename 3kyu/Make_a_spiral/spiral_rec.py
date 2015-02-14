#!/usr/bin/python


def can_left(arr,x,y):
    print arr[x+1][y-1],arr[x+1][y-2],arr[x][y-1],arr[x][y-2],arr[x-1][y-1],arr[x-1][y-2] 
    print arr[x+1][y-1]==0 and arr[x+1][y-2]==0 and arr[x][y-1]==0 and arr[x][y-2]==0 and arr[x-1][y-1]==0 and arr[x-1][y-2]==0 
    return arr[x+1][y-1]==0 and arr[x+1][y-2]==0 and arr[x][y-1]==0 and arr[x][y-2]==0 and arr[x-1][y-1]==0 and arr[x-1][y-2]==0

def can_right(arr,x,y):
    print arr[x+1][y+1],arr[x+1][y+2],arr[x][y+1],arr[x][y+2],arr[x-1][y+1],arr[x-1][y+2]
    print arr[x+1][y+1]==0 and arr[x+1][y+2]==0 and arr[x][y+1]==0 and arr[x][y+2]==0 and arr[x-1][y+1]==0 and arr[x-1][y+2]==0
    return arr[x+1][y+1]==0 and arr[x+1][y+2]==0 and arr[x][y+1]==0 and arr[x][y+2]==0 and arr[x-1][y+1]==0 and arr[x-1][y+2]==0

def can_down(arr,x,y):
    print arr[x+1][y+1],arr[x+2][y+1],arr[x+1][y],arr[x+2][y],arr[x+1][y-1],arr[x+2][y-1]
    print arr[x+1][y+1]==0 and arr[x+2][y+1]==0 and arr[x+1][y]==0 and arr[x+2][y]==0 and arr[x+1][y-1]==0 and arr[x+2][y-1]==0
    return arr[x+1][y+1]==0 and arr[x+2][y+1]==0 and arr[x+1][y]==0 and arr[x+2][y]==0 and arr[x+1][y-1]==0 and arr[x+2][y-1]==0

def can_up(arr,x,y):
    print arr[x-1][y+1],arr[x-2][y+1],arr[x-1][y],arr[x-2][y],arr[x-1][y-1],arr[x-2][y-1]
    print arr[x-1][y+1]==0 and arr[x-2][y+1]==0 and arr[x-1][y]==0 and arr[x-2][y]==0 and arr[x-1][y-1]==0 and arr[x-2][y-1]==0
    return arr[x-1][y+1]==0 and arr[x-2][y+1]==0 and arr[x-1][y]==0 and arr[x-2][y]==0 and arr[x-1][y-1]==0 and arr[x-2][y-1]==0

#ground=list()

def spiralize(size):
    ground=list()
    ground.append([1 for j in xrange(size+4)])
    #ground.append([0 for j in xrange(size+4)])
    for i in xrange(size+2): ground.append([1 if j==0 or j==size+3 else 0  for j in xrange(size+4)])
    #for i in xrange(size): ground.append([1 if j==0 or j==size+3 else 0  for j in xrange(size+4)])
    #ground.append([0 for j in xrange(size+4)])
    ground.append([1 for j in xrange(size+4)])
    rez=spiral(ground,2,2,size+2)
    rez=rez[2:-2]
    rez=map(lambda i: i[2:-2],rez)
    return rez

def spiral(arr, x, y, n):
    print "--------------"
    if not arr[0]: return []
    arr[x][y]=1

    for i in arr:
        print i
    print " @",x,',',y,'=',arr[x][y]

    # GO RIGHT
    print arr[x-1][y], arr[x-2][y]
    raw_input()
    if not (x-1>=0 and arr[x-1][y]==0 and arr[x-2][y]==0):
        print "TEST RIGHT"
        print " ",arr[x][y+1],arr[x][y+2]
        #if y+1<n and not arr[x][y+1] and arr[x][y+2]!=1 : 
        if can_right(arr,x,y):
            print "GO RIGHT"
            arr=spiral(arr,x,y+1,n)
    # GO DOWN
    #if x+1<n and not arr[x+1][y] and arr[x+2][y]!=1: 
    print "TEST DOWN"
    if can_down(arr,x,y):
        print "GO DOWN"
        arr=spiral(arr,x+1,y,n)
    # GO LEFT
    #if y-1>=0 and not arr[x][y-1] and arr[x][y-2]!=1:
    print "TEST LEFT"
    if can_left(arr,x,y):
        print "GO LEFT"
        arr=spiral(arr,x,y-1,n)
    # GO UP
    #if x-1>=0 and not arr[x-1][y] and arr[x-2][y]!=1: 
    print "TEST UP"
    if can_up(arr,x,y):
        print "GO UP"
        arr=spiral(arr,x-1,y,n)

    print "RETURN"

    return arr


for i in spiralize(20):
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
