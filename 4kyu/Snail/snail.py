#!/usr/bin/python

array = [
[1,2,3],
[8,9,4],
[7,6,5]
]

array_1 = [
[1,2,3],
[4,5,6],
[7,8,9]
]

array_2=[
[1,2],
[3,4]
]

array_3=[
[1]
]

array_4=[
[]
]

def snailpath(arr, x, y, n,path):
    print " ",n," @",x,',',y,'=',arr[x][y]
    print "PATH: ",path
    print "ARRAY: ",arr
    raw_input()
    if not arr[0]: return []
    path+=[arr[x][y]]
    arr[x][y]=0
    # GO RIGHT
    if not (x-1>=0 and arr[x-1][y]):
        if y+1<n and arr[x][y+1]: snailpath(arr,x,y+1,n,path)
    # GO DOWN
    if x+1<n and arr[x+1][y]: snailpath(arr,x+1,y,n,path)
    # GO LEFT
    if y-1>=0 and arr[x][y-1]: snailpath(arr,x,y-1,n,path)
    # GO UP
    if x-1>=0 and arr[x-1][y]: snailpath(arr,x-1,y,n,path)

    print "PATH: ",path
    return path

def snail(arr):
    return snailpath(arr, 0, 0, len(arr), [])


# snail([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]): 
# result: [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 17, 18, 19, 14, 13, 12, 11, 6, 7, 8, 9] 
# expect: [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
print snail([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
#print snail(array_2)
#print snail(array_3)
#print snail(array_4)
#print snail(array) 
#print "#=> [1,2,3,4,5,6,7,8,9]"
#print snail(array_1) 
#print "#=> [1,2,3,6,9,8,7,4,5]"
